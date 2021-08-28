import sqlite3
conn = sqlite3.connect("data_movies")

cur = conn.cursor()

#selects the record if the year_of_release is 2014

query2="select * from movies where Year_of_release=2014"
cur.execute(query2)

#fetchone fetches only the first record which satisfies the condition

data = cur.fetchone()

print("type of data is :",type(data))
print("\n")
print(data)

cur.close()
conn.close()
