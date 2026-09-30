import csv
import ast
import os
def display_all_students():
    with open("student.csv",'r') as stud:
        cr=csv.reader(stud)
        if os.path.getsize("student.csv")==0:
            print("student not found")
            return
        for s in cr:
            for i in s:
                x = ast.literal_eval(i)
                marks = x["marks"]
                total = sum(marks)
                average = total / 3

                if all(mark >= 40 for mark in marks):
                    status = "Pass"
                else:
                    status = "Fail"

                print("\nRegistration Number:", x["reg_no"])
                print("Name:", x["name"])
                print("Department:", x["department"])
                print("Marks:", marks)
                print("Total:", total)
                print("Average:", average)
                print("Status:", status)