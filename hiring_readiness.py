import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID: "))

# Get CGPA

cursor.execute("""
SELECT cgpa
FROM students
WHERE student_id=%s
""", (student_id,))

result = cursor.fetchone()

if result is None:
    print("Student Not Found!")
    conn.close()
    exit()

cgpa = result[0]

# Count Skills

cursor.execute("""
SELECT COUNT(*)
FROM skills
WHERE student_id=%s
""", (student_id,))

skills = cursor.fetchone()[0]

# Count Certifications

cursor.execute("""
SELECT COUNT(*)
FROM certifications
WHERE student_id=%s
""", (student_id,))

certs = cursor.fetchone()[0]

# Count Projects

cursor.execute("""
SELECT COUNT(*)
FROM projects
WHERE student_id=%s
""", (student_id,))

projects = cursor.fetchone()[0]

# Readiness Formula

score = (
    (cgpa * 5) +
    (skills * 10) +
    (certs * 10) +
    (projects * 15)
)

if score > 100:
    score = 100

print("Hiring Readiness Score =", score, "%")

if score >= 85:
    print("Status : Highly Employable")

elif score >= 65:
    print("Status : Job Ready")

elif score >= 40:
    print("Status : Needs Improvement")

else:
    print("Status : High Risk")

conn.close()