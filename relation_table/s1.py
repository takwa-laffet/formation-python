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
""" # creation des tables user et profile one to one
cors.execute("create table users(user_id int auto_increment primary key," \
" name varchar(255),email varchar(255), password varchar(255),role varchar(255))")
print("table users created successfully")
cors.execute("create table profile(profile_id int auto_increment primary key," \
" id_user int, bio varchar(255), FOREIGN KEY (id_user) REFERENCES users(user_id))")
print("table profile created successfully")
 """
""" cors.execute("insert into users(name,email,password,role)values('mohamed','mohamed.ali@example.com','1234','student')")
conn.commit() """
""" print("data inserted successfully")
cors.execute("insert into profile(id_user,bio)values(1,'i am a python student <3 <3')")
conn.commit()
print("data inserted successfully") """
""" cors.execute("insert into users(name,email,password,role)values('faten','faten@example.com','Pasword123!','student')")
conn.commit()
 """
""" cors.execute("insert into profile(id_user,bio)values(2,'i am a java student <3 <3')")
conn.commit()
print("data inserted successfully") """
#affichage des données one to one

""" cors.execute("select users.name,profile.bio from users Join profile on users.user_id = profile.id_user
 where users.name='mohamed'") """
""" for user in cors.fetchall():
    print(user) """""" 
med=cors.fetchone()
print(med) """
#many to many
""" cors.execute("create table courses(id int auto_increment primary key, name varchar(255),description varchar(255))")
 """
""" cors.execute("insert into courses(name,description)values('python','python course for beginners')")
cors.execute("insert into courses(name,description)values('java','java course for beginners')")
conn.commit()
print("table courses created successfully and data inserted successfully") 
 """
""" cors.execute("CREATE TABLE users_courses(id_user INT, id_cours INT, PRIMARY KEY (id_user, id_cours), FOREIGN KEY (id_user) REFERENCES users(user_id), FOREIGN KEY (id_cours) REFERENCES courses(id))")
 """
""" cors.execute("insert into users_courses(id_user,id_cours)values(1,7)")
conn.commit()

print("data inserted successfully")
cors.execute("insert into users_courses(id_user,id_cours)values(1,8)")
conn.commit()

print("data inserted successfully")
conn.commit()

cors.execute("insert into users_courses(id_user,id_cours)values(2,7)")
conn.commit()
print("data inserted successfully")

cors.execute("insert into users_courses(id_user,id_cours)values(2,8)")
print("2,8 data inserted successfully")
conn.commit()
 """
 #alter table users_courses add colon date
""" cors.execute("ALTER TABLE users_courses ADD COLUMN date varchar(255)")
conn.commit()
print("date column added successfully") """
# affichage des données many to many
cors.execute("select * from users_courses join users on users_courses.id_user=users.user_id join " \
"courses on users_courses.id_cours=courses.id")
for coursuser in cors.fetchall():
    print(coursuser)

