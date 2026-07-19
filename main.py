while True:

    print("\n===== CAREER INTELLIGENCE PLATFORM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Resume Score")
    print("4. Hiring Readiness")
    print("5. Skill Gap Analysis")
    print("6. Career Recommendation")
    print("7. Placement Prediction")
    print("8. Student Rankings")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        exec(open("add_student.py").read())

    elif choice == "2":
        exec(open("view_students.py").read())

    elif choice == "3":
        exec(open("resume_score.py").read())

    elif choice == "4":
        exec(open("hiring_readiness.py").read())

    elif choice == "5":
        exec(open("skill_gap.py").read())

    elif choice == "6":
        exec(open("career_recommendation.py").read())

    elif choice == "7":
        exec(open("placement_prediction.py").read())

    elif choice == "8":
    exec(open("student_ranking.py").read())

    elif choice == "9":
    print("Thank You!")
    break