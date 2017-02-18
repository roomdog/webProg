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
print ('<link href="webpage.css" rel = "stylesheet" type = "text/css" />')
print ("</head>")
print ("<body>")

# for row in locationResult:
# 	print ('<br> Login: ', row[0])

print ("<div>")
print ("<select>")
for row in locationResult:
	rowToPrint = row[0]
	print ("<option value=", rowToPrint, ">", rowToPrint , "</option>")
print ("</select>")
print ("<select>")
for row in locationResult:
	rowToPrint2 = row[0]
	print ("<option value=", rowToPrint2, ">", rowToPrint2 , "</option>")
print ("</select>")
print ("</div>")


print ("</body>")
print ("<html>")

cursor.close()
conn.close()
