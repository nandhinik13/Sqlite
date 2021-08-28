import sqlite3

conn = sqlite3.connect("data_movies")

print("Enter the Actress Name,which you want to update")
ac1 = input()

print("Enter the Director Name, which you want to update")
d1 = input()

query4 = "update movies set actress='" + ac1 + "' where director = '" + d1 + "'"

conn.execute(query4)
conn.commit()

conn.close()

print("Data Updated")
