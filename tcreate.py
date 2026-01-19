import sqlite3
conn=sqlite3.connect("dbase.db")
cursor=conn.cursor()
#cursor.execute("CREATE TABLE student (ID int primary key,Name varchar[20],Department varchar[10],Mark float,pwd varchar[10] NOT NULL)")
#cursor.execute("CREATE TABLE faculty(ID int primary key,name varchar[20],pwd varchar[10] NOT NULL)")
#cursor.execute("INSERT INTO faculty VALUES(?,?,?)",(100,"RAM",'100')) 

cursor.execute("SELECT * FROM student ")
user = cursor.fetchone()
for i in user:
    print(i)
conn.commit
conn.close
print("db done")