import sqlite3
conn = sqlite3.connect("data_movies")

cur = conn.cursor()

#selects the record if the actor name is ajith

query = "select * from movies where actor='Ajith'"
cur.execute(query)

#fetchall fetches all the records which satisfies the condition

data = cur.fetchall()

print("type of data is :",type(data))
print("\n")
print(data)

cur.close()
conn.close()
