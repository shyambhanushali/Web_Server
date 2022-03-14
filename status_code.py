import sys
from datetime import datetime


def status_code_200(body):
    '''
     Sent, with the contents of the file requested, if no other error codes are returned.
    '''
    # print("HTTP/1.1 200 OK\r\n\r\n")
    # sys.exit(0)
    response = "HTTP/1.1 200 OK\r\n"
    response += "Date: " + datetime.now().strftime('%a, %d %b %Y %I:%M:%S') + "\r\n"
    response += "\r\n"
    response += body
    print("200 response body: ", response)
    return str(response)


# status_code_200()


def status_code_201(body, location):
    '''
     Sent after a successful PUT command. The contents of the file created should be in the body of a 201 response and
     the file path (relative to the web root) should be returned in the location header.
    '''
    # print("Response code")
    # sys.exit(0)
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Location: " + location + "\r\n"
    response += "\r\n"
    response += body
    return response


def status_code_400():
    '''
    Sent if the HTTP parser indicates the HTTP request was not valid.
    '''
    response = "HTTP/1.1 400 Bad Request\r\n"
    response + "\r\n"
    response += "Bad Request"
    response += "\r\n"
    return response


def status_code_403():
    '''
    Sent if the HTTP server does not have permission to access the requested file
    '''

    response = "HTTP/1.1 400 Forbidden\r\n"
    response + "\r\n"
    response += "Forbidden"
    response += "\r\n"
    return response


def status_code_404():
    '''
    Sent if the HTTP server cannot find the file requested
    '''
    response = "HTTP/1.1 404 Not Found\r\n"
    response + "\r\n"
    response += "File Not Found"
    response += "\r\n"
    return response


def status_code_411():
    '''
    Sent if content-length is not set for POST requests
    '''

    response = "HTTP/1.1 411 Length Required\r\n"
    response + "\r\n"
    response += "Length Required"
    response += "\r\n"
    return response


def status_code_500():
    '''
    Sent as a default if the HTTP server or parser experiences an error
    from which it cannot recover while processing a request (for example, if the server experiences an exception)
    '''
    response = "HTTP/1.1 500 Internal Server Error\r\n"
    response + "\r\n"
    response += "Internal Server Error"
    response += "\r\n"
    return response


def status_code_501():
    '''
    Sent if the method specified in the HTTP request is not implemented in the server.
    '''

    response = "HTTP/1.1 501 Not Implemented\r\n"
    response + "\r\n"
    response += "Not Implemented"
    response += "\r\n"
    return response


def status_code_505():
    '''
    Sent if the HTTP server does not support the version of HTTP specified in the file (1.1 and 1.0 are permissible
    '''
    response = "HTTP/1.1 505 HTTP Version Not Supported\r\n"
    response + "\r\n"
    response += "HTTP Version Not Supported"
    response += "\r\n"
    return response
