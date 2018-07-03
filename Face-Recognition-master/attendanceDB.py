import sqlite3 as db
import datetime

def create():
    con = db.connect("attendance.db")
    con.execute("Create table if not exists Attendance(id INTEGER,name text, date Date, status text DEFAULT 'A', count INTEGER DEFAULT 1);")
    con.commit()
    con.close()

def enter(id):
    con = db.connect("attendance.db")
    con1 = db.connect("project.db")
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    name = con1.execute("Select * from Users where id = ?", (id,))
    data = name.fetchall()
    con.execute('''INSERT INTO Attendance(id, name, date)
                      VALUES(:id,:name, :date)''',
                {'id': id, 'name': data[0][1], 'date': date})
    con.commit()
    con.close()

def inc(id):
    con = db.connect("attendance.db")
    con.execute("UPDATE Attendance SET count = count + 1 WHERE id = ?",(id,))
    con.commit()
    num = con.execute("Select count from Attendance where id = ?", (id,))
    data =  num.fetchall()
    count = data[0][0]
    if ( count > 2) :
        con.execute("update Attendance set status = 'P' where id = ?", (id,))
        con.commit()
    con.close()

create()
#inc(1)
#enter(99)

"""con = db.connect("attendance.db")
date = datetime.datetime.today().strftime('%Y-%m-%d')
cur =con.cursor()
x =cur.execute("Select count from Attendance where id = ?", (99,))
data = x.fetchall()
print(data[0])
con.commit()"""""