

CGI : Common Gateway Interface 

Deploy a website part of Windows/Linux/Unix


Requirement :

1. OS : Linux(Amazon Linux)
	- Download, Install & Configure Utility Commands i.e. vim, curl, wget, unzip 
	- Download, Install & Configure Webserver i.e. Apache httpd 
	- yum install http* --skip-broken -y
	- systemctl start httpd.service
	- systemctl enable httpd.service
	- systemctl status httpd.service
	- cd /var/www/html
	- Created a file : index.html
	- Navigated to CGI folder i.e. /var/www/cgi-bin/
	- Created a file & Code : checkbox.py  
	- change the permissions : chmod 755 checkbox.py
	- Go to Browser and test the application

File Name : index.html 

<html>
<head>
<title>Python 7am Batch</title>
</head>

<body bgcolor="olive">

<h1> Welcome to Naresh IT </h1>

<h2> Select your course option </h2>
<form action="/cgi-bin/checkbox.py" method="GET" target="_blank">
First Name : <input type="" name="FirstName"/>
Last Name  : <input type="" name="LastName"/>
<input type="checkbox" name="Python" value="on" /> Python
<input type="checkbox" name="Perl" value="on" /> Perl
<input type="submit" value="Click Me!" />
</form>

</body>
</html>

# cd /var/www/cgi-bin/

# vi checkbox.py

#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('Python'):
        course_flag = "ON"
else:
   course_flag = "OFF"

if form.getvalue('Perl'):
   Perl_flag = "ON"
else:
   Perl_flag = "OFF"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Checkbox - Third CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> CheckBox Python is : %s</h2>" % course_flag)
print ("<h2> CheckBox Perl is : %s</h2>" % Perl_flag)
print ("</body>")
print ("</html>")


