import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

cursor = conn.cursor()

df = pd.read_excel("students.xlsx")

for index, row in df.iterrows():

    sql = """
    INSERT INTO students
    (name, age, cgpa, branch)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        row["name"],
        row["age"],
        row["cgpa"],
        row["branch"]
    )

    cursor.execute(sql, values)

conn.commit()

print("Excel Data Imported Successfully!")

conn.close()