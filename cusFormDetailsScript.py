#! /Python35/python
import cgi, cgitb, sys, mysql.connector

# to enable browser to show errors
cgitb.enable()
cardDetails = "carddetails"
cusDetails = "customerdetails"
name = ''
cursor = ''

# creates connection to sql database - local right now but looking to host somewhere central we can all access
conn = mysql.connector.connect(user='root',
							   password='',
							   host='localhost',
							   database='customer')
if conn.is_connected():
  cursor = conn.cursor(buffered=True)


#print ('content-type: text/html \n')
#print ""
#print "<link href="/webpage.css" rel = "stylesheet" type = "text/css" />"
#print "<html><head>"

form = cgi.FieldStorage() # collects and stores data from html form
title = form.getvalue('title')
fname = form.getvalue('fname')	# get values of form data fields sent by html form
sname = form.getvalue('sname')
dob = form.getvalue('dob')
email = form.getvalue('mail')
contact = form.getvalue('contact')
pword = form.getvalue('pword')


#sql statement to insert data from html form into customer database
sql = "INSERT INTO customerdetails (Title, Forename, Surname, DOB, Contact, Email, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
args = (title, fname, sname, dob, contact, email, pword, )
cursor.execute(sql, args)
conn.commit()

sql2 = "SELECT Customer_ID FROM customerdetails WHERE Email = %s"
args2 = (email,)
cursor.execute(sql2, args2)
conn.commit()
result = cursor.fetchone()
newResult = result[0]

sql3 = "INSERT INTO carddetails (Customer_ID) VALUES (%s) "
args3 = (newResult,)
cursor.execute(sql3, args3)
conn.commit()


print ('content-type: text/html \n')
print ("<HTML>")
print ("<head>")
print ('<link href="webpage.css" rel = "stylesheet" type = "text/css" />')
print ("</head>")
print ("<body>")

cardDetails = """
<header><a href="http://www.bannersketch.com" target="_blank"><img src="http://939e41ae03370909bc43-7080cc68367e890d409340077e3767c2.r98.cf3.rackcdn.com/1485807919.png" alt="Generated image" title="Free Banner by Bannersketch.com" style="border: 0px" align="left" /></a></header>
<nav>
<ul>
<li><a class="active" href="#home">Home</a></li>
<li><a href="#booking">Booking</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>
</nav>
<section>
<div>
<form name = "cardForm" action="paymentReceipt.py" method="post">
<label for="ctype">Card Type</label>
<select id="ctype" name="ctype">
<option value="visa">Visa</option>
<option value="master">Mastercard</option>
<option value="mastero">Mastero</option>
<option value="am">American Express</option>
</select>
<label for="cname">Name on Card</label>
<input type="text" id="cname" name="cname" required="Please enter the name on the card">
<label for="cno">Card Number</label>
<input type="text" id="cno" name="cno" required="Please enter the 16 digit card number">
<label for="expire">Expirey Date</label>
<input type="text" pattern="^((0[1-9])|(1[0-2]))\/*((2011)|(20[1-9][1-9]))$" id="expire" name="expire" placeholder="month-year" required="Please enter expirey date">
<label for="cvv">CVV</label>
<input type="text" pattern="^([0-9]{3,4})$" id="cvv" name="cvv" required="Please enter last 3 numbers on back of card">
<input type="submit" value="Pay Now">
</form>
</div>
"""
print (cardDetails)
print ("</body>")
print ("<html>")

cursor.close()
conn.close()
