import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Kedar1234#",database="demo1")
print("Connection established")
cursor=conn.cursor()
print("Cursor established")