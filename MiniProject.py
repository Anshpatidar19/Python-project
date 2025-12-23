#Count the number of student

numofstudents = int(input("Enter total students:"))


#Data Storage
studentData =[]

#inserting data
for i in range(numofstudents):
    print(f"Enter the Data of Student {i+1}")
    name = input("name")
    roll_no = int(input("roll_no"))
    marks = int(input("marks"))

    if marks > 95:
        grade = "A"
    elif marks > 80:
        grade = "B"
    elif marks > 60:
        grade = "C"
    elif marks >= 33:
        grade = "D"
    else:
        grade = "F"

    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    }
    studentData.append(students)
#Data Printing
print("\n All student Data: ")

for s in studentData:
    print(f"{s["name"]} - Roll Number:{s["roll_no"]} - marks {s["marks"]} - Grades{s["grade"]}")

#passed student
print("\n Student who are Passed: ")

for s in studentData:
    if s["marks"] >= 33:
        print(f"{s["name"]} - Marks:{s["marks"]}")
        
