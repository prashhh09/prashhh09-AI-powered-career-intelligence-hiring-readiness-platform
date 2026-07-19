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

skills = []

for row in cursor.fetchall():
    skills.append(row[0])

print("\n===== CAREER RECOMMENDATION =====")

if "Python" in skills and "SQL" in skills:
    print("Recommended Role : Data Analyst")

elif "Java" in skills:
    print("Recommended Role : Software Developer")

elif "Power BI" in skills:
    print("Recommended Role : Business Analyst")

else:
    print("Recommended Role : General IT Profile")

conn.close()