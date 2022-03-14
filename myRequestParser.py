"""
Working parser code
pass a request file, main() will use functions where it will check if the request is valid
and parse the request, store the components into dictionary and return
"""

import status_code
import sys

allowed_methods = ["GET", "POST", "PUT", "DELETE", "CONNECT", "HEAD"]
unaccepted_methods = ["PATCH", "OPTIONS", "LINK", "UNLINK"]
checklist = []
request_dict = {}


def usage():
    '''
    Print usage form
    python3 myRequestParser.py [http request file name]
    '''
    print("""
    Usage:Change permissions of the file and execute

          chmod +x myRequestParser.py \n
          ./myRequestParser.py [http request file name]
    """)

# def request_str():

#   if len(sys.argv) != 3:  # real val 2, temp=1
#       usage()
#       sys.exit(1)
#       pass
#   else:

#       with open(sys.argv[1], 'rb') as f:
#           req = f.read()
#           return req

def get_headers_body(request):
    request_line_and_headers = request.split("\\r\\n\\r\\n")
    headers = request_line_and_headers[0].split("\\r\\n")[1:]
    new_headers = []
    body = request_line_and_headers[1]
    name = []
    value = []
    host_count = 0
    for header in headers:
        new_headers.append(header)
    for header in new_headers:
        split_head = header.split(":")
        name.append(split_head[0])
        value.append(split_head[1])

    header_dict = dict(zip(name, value))
    if header_dict["Host"].lower() != " ":
        host_count += 1

    if host_count == 1:
        return header_dict, body

    return "ERROR_HEADER", "ERROR_BODY"


def check_method(method):
    request_dict["method"] = method.upper()
    if method.upper() in allowed_methods:
        request_dict["response_code"] = 200
    elif method.upper() in unaccepted_methods:
        request_dict["response_code"] = 501


def check_resource_uri(resource_uri):
    if resource_uri != " ":  ## Add request URI check
        checklist.append("True")
        request_dict["resource_uri"] = resource_uri
    else:
        request_dict["response_code"] = 400


def check_version(version):
    if version == "HTTP/1.1" or version == "HTTP/1.0":
        checklist.append("True")
        request_dict["version"] = version
    else:
        request_dict["response_code"] = 505


def check_request_line(request_line):  #############
    if len(request_line.split(" ")) != 3:
        request_dict["response_code"] = 400
    else:

        method = request_line.split(" ")[0][2:]
        check_method(method)
        resource_uri = request_line.split(" ")[1]
        check_resource_uri(resource_uri)
        version = request_line.split(" ")[2]
        check_version(version)


# def check_headers(headers):
# def http_request_parser(request):
#   # checklist = []
#   # allowed_methods = ["GET", "POST", "PUT", "DELETE", "CONNECT"]
#   request_dict = {}
#   request_dict["response_code"] = 200
#   # print(request_dict)
#   # request = request_str()
#   request_line = request.split(b"\r\n")[0].decode("utf-8")
#   check_request_line(request_line)
#   headers,body = get_headers_body(request)
#   request_dict["headers"] = headers
#   request_dict["body"] = body
#   return request_dict
def http_request_parser(request):
    request_dict["response_code"] = 200
    request_line = request.split("\\r\\n")[0]
    print(request_line)
    check_request_line(request_line)
    headers,body = get_headers_body(request)
    print(headers, body)
    request_dict["headers"] = headers
    request_dict["body"] = body
    # print(request_dict)
    # return request_dict


def main():
    var = http_request_parser()
    print(var)


if __name__ == "__main__":
    main()
