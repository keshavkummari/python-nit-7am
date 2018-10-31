Python CGI:

Example - 1:
*******************************************************************
File name: hello_get.py

#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (first_name, last_name)
print "</body>"
print "</html>"

*******************************************************************
Now, we need to create one more file:


*******************************************************************
http://192.168.234.101/cgi-bin/hello_get.py?first_name=Jessica%20Princess&last_name=Kummari

*******************************************************************

*******************************************************************

*******************************************************************

*******************************************************************