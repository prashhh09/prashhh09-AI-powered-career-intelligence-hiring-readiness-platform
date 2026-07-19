import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

cursor.execute("""
SELECT student_id, name, cgpa
FROM students
""")

students = cursor.fetchall()

ranking_list = []

for student in students:

    student_id = student[0]
    name = student[1]
    cgpa = student[2]

    # Skills Count

    cursor.execute("""
    SELECT COUNT(*)
    FROM skills
    WHERE student_id=%s
    """, (student_id,))

    skills = cursor.fetchone()[0]

    # Certifications Count

    cursor.execute("""
    SELECT COUNT(*)
    FROM certifications
    WHERE student_id=%s
    """, (student_id,))

    certs = cursor.fetchone()[0]

    # Projects Count

    cursor.execute("""
    SELECT COUNT(*)
    FROM projects
    WHERE student_id=%s
    """, (student_id,))

    projects = cursor.fetchone()[0]

    score = (
        cgpa * 5 +
        skills * 10 +
        certs * 10 +
        projects * 15
    )

    ranking_list.append(
        (name, round(score, 2))
    )

ranking_list.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\n===== STUDENT RANKINGS =====\n")

rank = 1

for student in ranking_list:

    print(
        f"Rank {rank}: {student[0]} | Score = {student[1]}"
    )

    rank += 1

conn.close()