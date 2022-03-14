import os
from pathlib import Path


def execute_php_script(request_uri, request_params, http_method, execute_php_file):
    php_script_output = ""
    if http_method == "GET":
        set_environment_configs_get(execute_php_file, request_params)
        php_script_output = os.popen("php-cgi").read()
        set_environment_configs_get("", "", remove_vars=True)
    elif http_method == "POST":
        request_params= request_params[0:-1]
        set_environment_configs_post(execute_php_file, request_params)
        php_script_output = os.popen("echo $BODY | php-cgi").read()
        set_environment_configs_post("", "", remove_vars=True)

    returnFromScript = parse_php_output(php_script_output)
    return returnFromScript;

def find_php_resource(file_name, php_files_path):
    globber = php_files_path.rglob('*.php')
    php_file_path = ""

    for php_file in globber:
        if php_file.name == file_name.strip("/"):
            php_file_path = php_file

    return php_file_path


def set_environment_configs_post(script_path, request_params, remove_vars=False):
    if remove_vars:
        os.environ.pop("GATEWAY_INTERFACE")
        os.environ.pop("SCRIPT_FILENAME")
        os.environ.pop("REQUEST_METHOD")
        os.environ.pop("REDIRECT_STATUS")
        os.environ.pop("SERVER_PROTOCOL")
        os.environ.pop("REMOTE_HOST")
        os.environ.pop("CONTENT_LENGTH")
        os.environ.pop("BODY")
        os.environ.pop("CONTENT_TYPE")
    else:
        os.environ["GATEWAY_INTERFACE"] = "CGI/1.1"
        os.environ["SCRIPT_FILENAME"] = str(script_path)
        os.environ["REQUEST_METHOD"] = "POST"
        os.environ["SERVER_PROTOCOL"] = "HTTP/1.1"
        os.environ["REMOTE_HOST"] = "127.0.0.1"
        os.environ["CONTENT_LENGTH"] = str(len(request_params))
        print(os.popen("echo $CONTENT_LENGTH").read())
        os.environ["BODY"] = request_params
        os.environ["CONTENT_TYPE"] = "application/x-www-form-urlencoded"
        os.environ["REDIRECT_STATUS"] = "0"


def set_environment_configs_get(script_path, request_params, remove_vars=False):
    if remove_vars:
        os.environ.pop("QUERY_STRING")
        os.environ.pop("SCRIPT_FILENAME")
        os.environ.pop("REQUEST_METHOD")
        os.environ.pop("REDIRECT_STATUS")
    else:
        os.environ["QUERY_STRING"] = request_params
        # print(os.popen("echo $QUERY_STRING").read())
        os.environ["SCRIPT_FILENAME"] = str(script_path)
        os.environ["REQUEST_METHOD"] = "GET"
        os.environ["REDIRECT_STATUS"] = "0"


def parse_php_output(php_output_data):
    print(php_output_data)
    php_print_lines = "\n".join(php_output_data.split("\n")[2:])
    return php_print_lines;
    # fullOutput = str();
    # if php_print_lines.len() <= 1:
    #     return php_print_lines;

    # for statement in php_print_lines:
    #     fullOutput+=statement+"\n"
    # return fullOutput.strip();
    # return php_output_data.split("\n")[-1];
    # output_split = php_output_data.split("\n\n")
    # body = output_split[1]

    # headers = []
    # headers_seperated = output_split[0].split("\n")
    # for header in headers_seperated:
    #     headers.append(header.strip())