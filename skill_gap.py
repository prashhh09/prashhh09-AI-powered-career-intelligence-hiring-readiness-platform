import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID: "))

cursor.execute("""
SELECT skill_name
FROM skills
WHERE student_id=%s
""", (student_id,))

student_skills = []

for row in cursor.fetchall():
    student_skills.append(row[0])

required_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Statistics"
]

missing = []

for skill in required_skills:

    if skill not in student_skills:
        missing.append(skill)

print("\n===== SKILL GAP REPORT =====")

if len(missing) == 0:
    print("No Skill Gap Found")

else:

    print("Missing Skills:")

    for skill in missing:
        print("-", skill)

conn.close()