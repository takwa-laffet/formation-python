import mysql.connector

# connecting to the database
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eco"
)
# creating a cursor object to execute SQL queries
cursor= conn.cursor()
""" 
#creation table user  #parent table
cursor.execute("create table users(id int auto_increment primary key, name varchar(255), email varchar(255))")
conn.commit()
print("table users created successfully")
#creation table comandes #child table
cursor.execute("create table commandes(id_commande int auto_increment primary key, id_user int, " \
"product varchar(255), FOREIGN KEY (id_user) REFERENCES users(id))")
conn.commit()
print("table commandes created successfully")
#insertion des données dans la table users
cursor.execute("insert into users(name,email)values('mohamed','mohamed@example.com')")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into users(name,email)values('faten','benkhader')")
conn.commit()
print("data inserted successfully")
#insertion des données dans la table commandes
cursor.execute("insert into commandes(id_user,product)values(1,'laptop')")
conn.commit()
print("data inserted successfully")
cursor.execute("insert into commandes(id_user,product)values(2,'phone')")
conn.commit()
print("data inserted successfully") """

#affichage des donnes
#affichage des commandes avec le nom user
""" cursor.execute("select commandes.product,users.name from commandes inner join users on commandes.id_user = users.id " \
"where users.name='faten'")
for c in cursor.fetchall():
    print(c) 

cursor.execute("select commandes.product,users.name from commandes join users on commandes.id_user=users.id where " \
"users.name='mohamed'")
for c in cursor.fetchall():
    print(c)
 """

#left join
""" cursor.execute("insert into users(name,email)values('sami','sami@example.com')")
conn.commit()
print("data inserted successfully")
cursor.execute("select users.name,commandes.product from users left join commandes on users.id = commandes.id_user")

for c in cursor.fetchall():
    print(c)
 """
#right join 

#table fromation #many to many
cursor.execute("create table formations(id int auto_increment primary key, name varchar(255), description varchar(255))")
conn.commit()
print("table formations created successfully")
#table users_formations
cursor.execute("create table users_formations(id_user int, id_formation int, PRIMARY KEY (id_user, id_formation), " \
"FOREIGN KEY (id_user) REFERENCES users(id), FOREIGN KEY (id_formation) REFERENCES formations(id))")
conn.commit()
print("table users_formations created successfully")
#insertion des données dans la table formations
cursor.execute("insert into formations(name,description)values('python','python course for beginners')")
conn.commit()
cursor.execute("insert into formations(name,description)values('java','java course for beginners')")
conn.commit()
print("data inserted successfully")
#insertion des données dans la table users_formations
cursor.execute("insert into users_formations(id_user,id_formation)values(1,1)")
conn.commit()
print("data inserted successfully")

cursor.execute("select users.name,formations.name from users right join users_formations on users.id = users_formations.id_user" \
" right join formations on users_formations.id_formation = formations.id")
for c in cursor.fetchall():
    print(c)
