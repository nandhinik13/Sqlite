import sqlite3
conn = sqlite3.connect("data_movies")

cur = conn.cursor()
#selects all the records
query3 = "select * from movies"
cur.execute(query3)

#fetchall fetches all records from the table
data = cur.fetchall()

print("type of data is :",type(data))
print("\n")

for d in data:
    print(d)

cur.close()
conn.close()
