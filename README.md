
# Project B: Writing a Web Server


**Building a web server in python without using any external libraries**

Dependencies:

Install php-cgi library in Ubuntu:

sudo apt-get update -y


sudo apt-get install -y php-cgi


USAGE:
python3 server.py 127.0.0.1 8000 #http


python3 server.py 127.0.0.1 8000 private.key public.cert #https

GET request to 127.0.0.1:8000/handleGet.php?firstName=Virat&lastName=Kohli


POST request to 127.0.0.1:8000/handlePost.php where body=firstName=Virat&lastName=Kohli

Attacking the webserver: Check out the **attacking_server.pdf **
