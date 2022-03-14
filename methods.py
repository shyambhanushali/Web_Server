'''
GET, POST,  PUT, DELETE, CONNECT(optional), HEAD(optional)

'''
from pathlib import Path
import myRequestParser
import status_code
from PHP_config import execute_php_script
import os

# supported_methods_dict = {
#     "1": mget()
#     "2": mpost()
#     "3": mput()
#     "4": mdelete()
#     "5": mconnecT()
# }

PHP_RESOURCES = "PHP-Resources"


def mget(request_dict):
    current_path = Path.cwd()
    requested_path = Path(request_dict["resource_uri"])
    final_path = Path(str(current_path) + os.sep + PHP_RESOURCES + str(requested_path))
    if len(request_dict['resource_uri'].split("?")) == 2:
        req_filename, req_parameters = request_dict['resource_uri'].split("?")

    directory_path = Path(str(current_path) + os.sep + PHP_RESOURCES + req_filename)
    if directory_path.exists():
        try:
            if directory_path.suffix == ".php" and requested_path != "":
                outputBody = execute_php_script(requested_path, req_parameters, request_dict['method'], directory_path)
                print("outputBody from GET: ", outputBody)
                return status_code.status_code_200(outputBody)
        except PermissionError:
            return status_code.status_code_403()
    return status_code.status_code_404()


def mpost(request_dict):
    print("ENTERING POST METHOD!")
    if request_dict['headers']['Content-Length'] is None or request_dict['headers']['Content-Length'] == "":
        return status_code.status_code_411()

    current_path = Path.cwd()
    requested_path = Path(request_dict["resource_uri"])
    final_path = Path(str(current_path) + os.sep + PHP_RESOURCES + str(requested_path))
    if len(request_dict['resource_uri'].split(os.sep)) > 1:
        req_filename = request_dict['resource_uri'].split(os.sep)[-1]

    directory_path = Path(str(current_path) + os.sep + PHP_RESOURCES + os.sep + req_filename)
    if directory_path.exists():
        try:
            outputBody = execute_php_script(requested_path, request_dict['body'], "POST", directory_path)
            print("outputBody: ", outputBody)
            return status_code.status_code_200(outputBody)
        except PermissionError:
            return status_code.status_code_403()
    return status_code.status_code_404()


def mput(request_dict):
    current_path = Path.cwd()
    requested_path = Path(request_dict["resource_uri"])
    final_path = Path(str(current_path) + os.sep + PHP_RESOURCES + str(requested_path))
    body = request_dict["body"]
    final_path.write_text(body)

    return status_code.status_code_201(body, str(requested_path))


def mdelete(request_dict):
    current_path = Path.cwd()
    requested_path = Path(request_dict["resource_uri"])
    final_path = Path(str(current_path) + os.sep + PHP_RESOURCES + str(requested_path))
    if final_path.exists():
        final_path.unlink()
        return status_code.status_code_200(f"{requested_path} FILE DELETED SUCCESSFULLY")
    else:
        return status_code.status_code_404()


def mconnect(request_dict):
    # The authority form(request URI) is only used by the CONNECT method
    print("Function connect")


def mhead(request_dict):
    return status_code.status_code_200("")