#! /Python35/python
import cgi, cgitb, sys, mysql.connector

# to enable browser to show errors
cgitb.enable()
table = "customerdetails"
cusDetails = "customerdetails"
name = ''
cursor = ''

# creates connection to sql database - local right now but looking to host somewhere central we can all access
conn = mysql.connector.connect(user='root',
							   password='',
							   host='localhost',
							   database='customer')
if conn.is_connected():
  cursor = conn.cursor(buffered = True)

#print ('content-type: text/html \n')

form = cgi.FieldStorage()
uname = form.getvalue('uname')
pword = form.getvalue('pword')

sql = "SELECT Email, Password FROM customerdetails WHERE Email = %s AND Password = %s"
args = (uname, pword,)
cursor.execute(sql, args)
conn.commit()
result = cursor.fetchmany()

#while result:
#for uname, pword, in result:
	#print ('<br> Login: ', uname, pword,)
print ('content-type: text/html \n')
print ("<HTML>")
print ("<head>")
print ('<link href="webpage.css" rel = "stylesheet" type = "text/css" />')
print ("</head>")
print ("<body>")

login = """
<header> <a href="homepage.html" target="_blank"><img src="http://939e41ae03370909bc43-7080cc68367e890d409340077e3767c2.r98.cf3.rackcdn.com/1485807919.png" alt="Generated image" title="Free Banner by Bannersketch.com" style="border: 0px" align="left" /></a></div>
<nav>
<ul>
<li><a class="active" href="homepage.html">Home</a></li>
<li><a href="customerSignUp_v_1.3.html" >Booking</a></li>
<li><a href="#about">About</a></li>
<li><a href="#contact">Contact</a></li>

</ul>
</nav>
</header>

"""
print (login)
print ("</body>")
print ("</html>")
cursor.close()
conn.close()
