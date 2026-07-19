import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for row in records:
    print(row)

conn.close()