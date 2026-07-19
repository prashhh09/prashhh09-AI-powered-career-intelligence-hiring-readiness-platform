import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="career_intelligence"
)

query = "SELECT * FROM students"

df = pd.read_sql(query, conn)

df.to_excel(
    "student_report.xlsx",
    index=False
)

print("Excel Report Generated!")

conn.close()