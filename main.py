import sqlite3;
con = sqlite3.connect("metanit.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE people (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, age INTEGER)""")
cursor.execute("INSERT INTO people (name,age) VALUES ('Tom',38)")
bob=('Bob',42)
cursor.execute("INSERT INTO people (name,age) VALUES (?,?)",bob)
peopleList=[("Sam",23),("John",27),("Rain",19),("Alex",58)]
cursor.executemany("INSERT INTO people(name,age) VALUES (?,?)",peopleList)
con.commit()

cursor.execute("SELECT * FROM people")
print(cursor.fetchall())
cursor.execute("SELECT * FROM people")
for person in cursor.fetchall():
    print(f"{person[0]} - {person[1]} - {person[2]}")
cursor.execute("SELECT * FROM people")
print(cursor.fetchmany(3))
cursor.execute("SELECT * FROM people")
print(cursor.fetchone())
cursor.execute("SELECT name,age FROM people WHERE id=3")
name,age = cursor.fetchone()
print(f"Name:{name}  Age:{age}")
