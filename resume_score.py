import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID: "))

cursor.execute(
"""
SELECT COUNT(*)
FROM skills
WHERE student_id=%s
""",
(student_id,)
)

skills = cursor.fetchone()[0]

cursor.execute(
"""
SELECT COUNT(*)
FROM certifications
WHERE student_id=%s
""",
(student_id,)
)

certs = cursor.fetchone()[0]

cursor.execute(
"""
SELECT COUNT(*)
FROM projects
WHERE student_id=%s
""",
(student_id,)
)

projects = cursor.fetchone()[0]

score = (
skills*10 +
certs*15 +
projects*20
)

if score > 100:
    score = 100

print("Resume Score =", score)

conn.close()