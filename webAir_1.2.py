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

sql = "SELECT Name FROM locationtable"
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
print ("<form name = booking1>")
print ("<label for = depart>Departure</label>")
print ("<select id =departure name =departure>")
for row in locationResult:
	rowToPrint = row[0]
	print ("<option value=", rowToPrint, ">", rowToPrint , "</option>")
print ("</select>")
print ("<input type=submit value=select Departure Point>")
print ("</form>")

form = cgi.FieldStorage()
departureLoc = form.getvalue('departure')

#print ("<br>", departureLoc,)

if departureLoc == 'Bristol':
    sql = "SELECT Destination FROM bristol "
    cursor.execute(sql)
    conn.commit()
    destinationResult = cursor.fetchall()
elif departureLoc == 'London':
    sql = "SELECT Destination FROM london"
    cursor.execute(sql)
    conn.commit()
    destinationResult = cursor.fetchall()
elif departureLoc == 'Glasgow':
    sql = "SELECT Destination FROM glasgow"
    cursor.execute(sql)
    conn.commit()
    destinationResult = cursor.fetchall()
elif departureLoc == 'Newcastle':
    sql = "SELECT Destination FROM newcastle"
    cursor.execute(sql)
    conn.commit()
    destinationResult = cursor.fetchall()

if departureLoc == 'Bristol':
    sql = "SELECT departTime FROM bristol "
    cursor.execute(sql)
    conn.commit()
    destinationTime = cursor.fetchall()
elif departureLoc == 'London':
    sql = "SELECT departTime FROM london"
    cursor.execute(sql)
    conn.commit()
    destinationTime = cursor.fetchall()
elif departureLoc == 'Glasgow':
    sql = "SELECT departTime FROM glasgow"
    cursor.execute(sql)
    conn.commit()
    destinationTime = cursor.fetchall()
elif departureLoc == 'Newcastle':
    sql = "SELECT departTime FROM newcastle"
    cursor.execute(sql)
    conn.commit()
    destinationTime = cursor.fetchall()


print ("<form name = booking2>")
print ("<label for = dest>Destination</label>")
print ("<select id = destination name = Destination>")
for row in destinationResult:
	destinationToPrint = row[0]
	print ("<option value=", destinationToPrint, ">", destinationToPrint , "</option>")

print ("</select>")
print ("<label for = time>Departure Time</label>")
print ("<select id = time name = time>")
for row in destinationTime:
    timeToPrint = row[0]
    print ("<option value=", timeToPrint, ">", timeToPrint, "</option>")
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
print ("</form>")
print ("</div>")


print ("</body>")
print ("</html>")

cursor.close()
conn.close()
