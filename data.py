import sqlite3

conn = sqlite3.connect("data_movies")

print("Enter Movie name : ")
m = input()

print("Enter Actor name : ")
a = input()

print("Enter Actress name : ")
ac = input()

print("Enter Director name : ")
d = input()

print("Enter the year of release : ")
y = input()

query = "insert into movies(name,actor,actress,director,year_of_release) values('" + m + "','" + a + "','" + ac + "','" + d + "'," + y + ")"
conn.execute(query)
conn.commit()
conn.close()

print("Data saved")