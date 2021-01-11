import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="ks617",
    password="Komal",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("create table customers(name VARCHAR (255),address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)