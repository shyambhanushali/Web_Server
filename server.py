
import sys
import status_code
import pathlib
import Connection_Utils
import logging
import pathlib
import socket

def usage():
    '''
    Print usage form
    python3 myRequestParser.py [http request file name]
    '''
    print("""
    Usage:Change permissions of the file and execute

          chmod +x server.py \n
          ./server.py [IP] [PORT] [path to x509 crt or pem file] [path to private key paired with x509 cert]
    """)

    '''
    Uncomment and remove request_Str method both do the same thing but with additional checks
    '''

def collect_info():
    '''
    Returns data of the http request file
    '''
    data = {}
    if len(sys.argv) == 3:
        ip_addr = sys.argv[1]
        port = sys.argv[2]
        data["IP_ADDRESS"] = ip_addr
        data["PORT"] = port
        data["CONNECTION_TYPE"] = "http"

    elif len(sys.argv) == 5:
        ip_addr = sys.argv[1]
        port = sys.argv[2]
        x509_path = pathlib.Path(sys.argv[3])
        if x509_path.exists():
            pass
        else:
            print("Path to certificate not found")
            sys.exit(1)

        priv_key = pathlib.Path(sys.argv[4])
        if priv_key.exists():
            pass
        else:
            print("Path to private key not found")
            sys.exit(1)

        data["IP_ADDRESS"] = ip_addr
        data["PORT"] = port
        data["CONNECTION_TYPE"] = "https"
        data["X509_PATH"] = str(x509_path)
        data["PRIVATE_KEY_PATH"] = str(priv_key)
    else:
        usage()
        sys.exit(1)
    return data


"""
python3 server.py 127.0.0.1 80 test1.txt testerfile.txt 
{'IP_ADDRESS': '127.0.0.1', 'PORT': '80', 'CONNECTION_TYPE': 'https', 'X509_PATH': PosixPath('test1.txt'), 'PRIVATE_KEY_PATH': PosixPath('testerfile.txt')}
"""
def main():
    data = collect_info()    # Data requrired to start
    # print(data)
    try:
        Connection_Utils.listener(data)
    except Exception:
        status_code.status_code_500()


main()
# python server.py 127.0.0.1 8000


