import csv
import os
import ast
def add_student():
    with open("student.csv",'a',newline='') as stu:
        cw=csv.writer(stu)
    with open("student.csv",'r') as stud:
        cr=csv.reader(stud)
        if os.path.getsize("student.csv")==0:
            students = []
            reg_no = input("Enter Registration Number: ")
            name = input("Enter Name: ")
            department = input("Enter Department: ")

            marks = (
                float(input("Enter marks in Subject 1: ")),
                float(input("Enter marks in Subject 2: ")),
                float(input("Enter marks in Subject 3: "))
            )

            student = {
                "reg_no": reg_no,
                "name": name,
                "department": department,
                "marks": marks
            }

            students.append(student)
            with open("student.csv", 'a', newline='') as stud:
                cw = csv.writer(stud)
                cw.writerow(students)
            print("Student added successfully.")
        else:
            list1=[]
            reg_no = input("Enter Registration Number: ")
            for i in cr:
                for x in i:
                    s=ast.literal_eval(x)
                    list1.append(s["reg_no"])
            if reg_no in list1:
                print("Registration number already entered")
            else:
                students = []
                name = input("Enter Name: ")
                department = input("Enter Department: ")

                marks = (
                    float(input("Enter marks in Subject 1: ")),
                    float(input("Enter marks in Subject 2: ")),
                    float(input("Enter marks in Subject 3: "))
                )

                student = {
                    "reg_no": reg_no,
                    "name": name,
                    "department": department,
                    "marks": marks
                }

                students.append(student)
                with open("student.csv", 'a', newline='') as stud:
                    cw = csv.writer(stud)
                    cw.writerow(students)
                print("Student added successfully.")