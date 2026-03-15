import mysql.connector

# connecting to the database
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db"
)
# creating a cursor object to execute SQL queries
cors= conn.cursor()
""" cors.execute("SHOW DATABASES") # executing a SQL query to show all databases
 """
""" cors.execute("create table users(id int auto_increment primary key," \
"name varchar(255),pernom varchar(255),email varchar(255) )")
print("table created successfully") """

""" 
#-------------------crud-------------------------------
cors.execute("insert into users(name,pernom,email)values('mohamed','ali','mohamed.ali@example.com')")
conn.commit()
print("data inserted successfully")
nom="takwa"
pp="bensalem"
e="takwa.bensalem@example.com"
cors.execute("insert into users(name,pernom,email)values(%s,%s,%s)",(pp,nom,e))
conn.commit()
print("data inserted successfully") """
""" cors.execute("SELECT * FROM users")
users =cors.fetchall()
for user in users:
    print(user)
cors.execute("select email from users")
emails=cors.fetchall()
for email in emails:
    print(email)
cors.execute("select * from users where id=8")
user=cors.fetchone()
print(user)
cors.execute("select name ,email from users where id=9")
user=cors.fetchone()
print(user)
cors.execute("select name ,email from users ")
users=cors.fetchall()
for user in users:
    print(user)
cors.execute("update users set name='takwa',pernom='bensalem' where id=9")
conn.commit()
cors.execute("select name ,email from users where id=9")
user=cors.fetchone()
print(user)
cors.execute("delete from users where id=9")
conn.commit()
cors.execute("select name ,email from users where id=9")
user=cors.fetchone()
print(user)
 """
#---------------------------------------------------------------
#update table
""" cors.execute("alter table users add column age int")
conn.commit() """
#delete column
""" cors.execute("alter table users drop column email")
conn.commit()
"""
#rename column
""" cors.execute("alter table users change name nom varchar(255)")
conn.commit()
 """
 #rename table
""" cors.execute("alter table users rename to utilisateurs")
conn.commit()
 """
#drop table
""" cors.execute("drop table utilisateurs")
conn.commit() """
#drop database
cors.execute("drop database db")
conn.commit()

 #show all databases in the MySQL server
""" for i in cors:
    print(i)
 """
cors.close()
conn.close()