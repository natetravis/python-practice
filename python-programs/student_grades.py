student_grades ={}

number_of_students = int(input("Enter the number of students: "))

for i in range(number_of_students):
    name = input("Enter students name: ")
    grades = list(map(int, input(f"Enter grades for {name}, seperated by spaces: ").split()))
    student_grades[name] = grades

print("\nStudent Grades: ")
for student, grades in student_grades.items():
    print(f"{student}: {grades}")