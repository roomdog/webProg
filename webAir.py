#! /Python35/python
import cgi, cgitb, sys, mysql.connector

# to enable browser to show errors
cgitb.enable()
locations = "locations"
name = ''
cursor = ''

# creates connection to sql database - local right now but looking to host somewhere central we can all access
conn = mysql.connector.connect(user='root',
							   password='',
							   host='localhost',
							   database='locations')
if conn.is_connected():
  cursor = conn.cursor(buffered=True)

sql = "SELECT Destination FROM bristol"
cursor.execute(sql)
conn.commit()
locationResult = cursor.fetchall()


print ('content-type: text/html \n')
print ("<HTML>")
print ("<head>")
print ('<link href="newcss.css" rel = "stylesheet" type = "text/css" />')
print ("</head>")
print ("<body>")

nav = """
<nav>
<ul>
<li><a class="active" href="#home">Home</a></li>
<li><a href="#booking">Booking</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>
</nav>
"""
print (nav)
print("<br>")
print ("<div class = center>")
print ("<form name = booking>")
print ("<label for = depart>Departure</label>")
print ("<select id =departure name =departure>")
for row in locationResult:
	rowToPrint = row[0]
	print ("<option value=", rowToPrint, ">", rowToPrint , "</option>")
print ("</select>")
print ("<label for = dest>Destination</label>")
print ("<select id = destination name = Destination>")
for row in locationResult:
	rowToPrint2 = row[0]
	print ("<option value=", rowToPrint2, ">", rowToPrint2 , "</option>")
print ("</select>")
print ("<label for = nop>Number of passengers</label>")
print ("<select id =nop name =nop>")
print ("<option value = 1>1</option>")
print ("<option value = 2>2</option>")
print ("<option value = 3>3</option>")
print ("<option value = 4>4</option>")
print ("<option value = 5>5</option>")
print("</select>")
print ("<label for = noc>Number of children</label>")
print ("<select id =noc name =noc>")
print ("<option value = 1>1</option>")
print ("<option value = 2>2</option>")
print ("<option value = 3>3</option>")
print ("<option value = 4>4</option>")
print ("<option value = 5>5</option>")
print ("</select>")
print ("</div>")


print ("</body>")
print ("</html>")

cursor.close()
conn.close()
