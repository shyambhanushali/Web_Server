
# Project B: Writing a Web Server


**Building a web server in python without using any external libraries**

<h2>Dependencies:</h2>

Install php-cgi library in Ubuntu:

<b>sudo apt-get update -y


sudo apt-get install -y php-cgi</b>


USAGE:

<b>python3 server.py 127.0.0.1 8000 #http


python3 server.py 127.0.0.1 8000 private.key public.cert #https</b>

<h2> Send Requests </h2>

GET request to 127.0.0.1:8000/handleGet.php?firstName=Virat&lastName=Kohli


POST request to 127.0.0.1:8000/handlePost.php where body=firstName=Virat&lastName=Kohli

<h2> Attacking the server </h2>
Attacking the webserver: Check out the <b>attacking_server.pdf</b>
