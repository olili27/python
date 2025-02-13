import sqlite3

con = sqlite3.connect("people.db")
# con = sqlite3.connect(":memory:") # connect to a database in memory

# DATATYPES =================
# null
# integer
# real
# text
# blob

cursor = con.cursor()

cursor.execute("create table if not exists person(name text, age integer)")

# cursor.execute("delete from person")
# cursor.executemany("insert into person values(?, ?)", [(6, "tom"), ("dan", 30)])
person = {
    "age": 43,
    "name": "ojuliues",
    "hey-ther": "test"
}
cursor.execute("insert into person values(:name, :age)", person)
print(cursor.execute("select * from person").fetchall())
# print(cursor.execute("select * from person where name = :name", person).fetchall())
con.commit()