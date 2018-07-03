import sqlite3 as l
id= 151500294
con = l.connect("project.db")
#a = [(1,"alex","us"),(2,"jon","nz")]
con.execute("Create table if not exists Users(id INTEGER,name text);")
#con.execute("Insert into Users values (?,?)",(12,"India"))
#con.executemany("Insert into user1 values (?,?,?)",a)
x =con.execute("Select * from Users ")
#cur =con.cursor()
#x =cur.execute("Select * from user1")
data = x.fetchall()
for i in data:
    print(i)