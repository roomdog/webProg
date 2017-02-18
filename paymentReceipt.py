#! /Python35/python
import cgi, cgitb, sys, mysql.connector

# to enable browser to show errors
cgitb.enable()

#table = ""
#cusDetails = ""
name = ''
cursor = ''

# creates connection to sql database - local right now but looking to host somewhere central we can all access
conn = mysql.connector.connect(user='root',
							   password='',
							   host='localhost',
							   database='customer')
if conn.is_connected():
  cursor = conn.cursor()

form = cgi.FieldStorage() # collects and stores data from html form
ctype = form.getvalue('ctype')
cname = form.getvalue('cname')	# get values of form data fields sent by html form
cno = form.getvalue('cno')
expire = form.getvalue('expire')
cvv = form.getvalue('cvv')

#sql statement to insert data from html form into customer database
sql = "INSERT INTO carddetails (NameOnCard, CardNumber, ExpDate, CVV, CardType) VALUES (%s, %s, %s, %s, %s)"
args = (cname, cno, expire, cvv, ctype )
cursor.execute(sql, args)
conn.commit()

print ('content-type: text/html \n')
print ("<HTML>")
print ("<head>")
print ('<link href="webpage.css" rel = "stylesheet" type = "text/css" />')
print ("</head>")
print ("<body>")
nav = """
<header> <a href="homepage.html" target="_blank"><img src="http://939e41ae03370909bc43-7080cc68367e890d409340077e3767c2.r98.cf3.rackcdn.com/1485807919.png" alt="Generated image" title="Free Banner by Bannersketch.com" style="border: 0px" align="left" /></a></div>
<nav>
<ul>
<li><a class="active" href="homepage.html">Home</a></li>
<li><a href="customerSignUp_v_1.3.html" >Booking</a></li>
<li><a href="#about">About</a></li>
<li><a href="#contact">Contact</a></li>

</ul>
</nav>
</header> """
print (nav)
print ("</body>")
print ("</html>")

cursor.close()
conn.close()
