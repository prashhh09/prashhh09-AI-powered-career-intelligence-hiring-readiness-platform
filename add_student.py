import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

name = input("Enter Name: ")
age = int(input("Enter Age: "))
cgpa = float(input("Enter CGPA: "))
branch = input("Enter Branch: ")

sql = """
INSERT INTO students
(name,age,cgpa,branch)
VALUES (%s,%s,%s,%s)
"""

values = (name,age,cgpa,branch)

cursor.execute(sql, values)

conn.commit()

print("Student Added Successfully!")

conn.close()