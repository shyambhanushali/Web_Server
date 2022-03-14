from myRequestParser import http_request_parser, request_dict
import methods
import status_code
import socket
import ssl
import logging
import threading
import os

THREADS = 5


# Logging function

def logs(request_line):
    logging.basicConfig(level=logging.DEBUG, filename='Log_File.txt', filemode='a', format='%(asctime)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info(request_line)

"""
Handler handles all the incoming requests and sends the response
"""
def handler(sock):
    response = ""
    try:
        request = get_request(sock)
        print("============== start of request")
        print(request)
        print("=============== end of request")
        # parser.request_dict
        http_request_parser(request)
        # request_dict = parser.request_dict
        print("++++++++++++++++++ start of DICT")
        print(request_dict)
        print("++++++++++++++++++++++++ end of dict")

        request_line = request_dict["method"] + " " + request_dict["resource_uri"] + " " + request_dict["version"]
        logs(request_line)

        # parser.print_request_dict(request_dict)

        if request_dict["response_code"] != 200:
            response = http_status_code(request_dict["response_code"])
        else:
            response = execute_method(request_dict)
        # print("++++++++++++++++++ start of RESPONSE")
        # print(response)
        # print("++++++++++++++++++++++++ end of RESPONSE")
    except Exception:
        response = status_code.status_code_500()

    sock.sendall(response.encode())
    sock.close()


def http_status_code():
    if response_code == "400":
        return status_code.status_code_400()
    elif response_code == "501":
        return status_code.status_code_501()
    elif response_code == "505":
        return status_code.status_code_505()


def execute_method(request_dict):
    response = ""
    method = request_dict["method"]
    if method == "GET":
        response = methods.mget(request_dict)
    elif method == "POST":
        response = methods.mpost(request_dict)
    elif method == "PUT":
        response = methods.mput(request_dict)
    elif method == "DELETE":
        response = methods.mdelete(request_dict)
    elif method == "CONNECT":
        response = methods.mconnect(request_dict)
    elif method == "HEAD":
        response = methods.mhead(request_dict)

    return response


def get_request(sock):
    return str(sock.recv(1024))

"""
The listener starts the server
Takes in input data dict from the command line
"""
def listener(data):
    # Start the server with the arguments given

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 + tcp
    s.bind((data["IP_ADDRESS"], int(data["PORT"])))
    # s.bind(("127.0.0.1", int(8000)))

    print("Starting the web server")
    s.listen(THREADS)

    while True:
        conn, addr = s.accept()
        # conn.send(Response_Codes.respond_with_200().encode())  # Remove
        if data["CONNECTION_TYPE"] == "https":
            conn = https_socket(conn, str(data["X509_PATH"]), str(data["PRIVATE_KEY_PATH"]))
        t = threading.Thread(target=handler, args=(conn,))
        t.start()

"""
Create a https_socket
"""
def https_socket(conn, x509_cert, private_key):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=x509_cert, keyfile=private_key, password=None)
    return context.wrap_socket(conn, server_side=True)