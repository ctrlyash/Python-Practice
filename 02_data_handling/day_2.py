"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name: ").strip()
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists")
            continue

        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks")
    return students       

def display_reports(students):
    if not students:
        print("No student data ❌")
        return
    
    marks =list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks)/ len(marks)

    topper = [name for name, score in students.items() if score == max_score]
    bottommer = [name for name, score in students.items() if score == min_score]

    print("\n Students marks report 📝")
    print("-"*30)
    print(f"Total students: {len(students)}")
    print(f"Average marks for students: {average:.2f}")
    print(f"Highest marks: {max_score} by {', '.join(topper)}")
    print(f"Lowest marks: {min_score} by {', '.join(bottommer)}")\
    
    print("-"*30)
    print("Detailed Marks 📝")
    for name, score in students.items():
        print(f" - {name}: {score}")


students = collect_student_data()
display_reports(students)

# Enter the student name: Yash
# Enter marks for Yash: 95
# Enter the student name: Vrinda
# Enter marks for Vrinda: 96
# Enter the student name: Rehan
# Enter marks for Rehan: 93
# Enter the student name: Lakshya
# Enter marks for Lakshya: 91
# Enter the student name: done

#  Students marks report 📝
# ------------------------------
# Total students: 4
# Average marks for students: 93.75
# Highest marks: 96.0 by Vrinda
# Lowest marks: 91.0 by Lakshya
# ------------------------------
# Detailed Marks 📝
#  - Yash: 95.0
#  - Vrinda: 96.0
#  - Rehan: 93.0
#  - Lakshya: 91.0

