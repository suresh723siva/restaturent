#!C:\python\python.exe
import cgi
import mysql.connector 
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Logined</h1>")
#1. Frontend to Backend
data=cgi.FieldStorage()
Name=data.getvalue("name")
Mobile=data.getvalue("mobile")
Password=data.getvalue("pass")
print("<i>",Name,Mobile,Password,"</i>")
#2.Backend to Database

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="restaurent"
)
mycursor=DB.cursor()
sql="INSERT INTO login(Name,MobileNumber,Password) values (%s,%s,%s)"
values=(Name,Mobile,Password)
mycursor.execute(sql,values)
DB.commit()
print("</body>")
print("</html>")