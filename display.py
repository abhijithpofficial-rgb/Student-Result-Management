import csv
import ast
def display_result():
    reg_no = input("Enter Registration Number: ")
    list=[]
    with open("student.csv",'r') as stud:
        cr=csv.reader(stud)
        for s in cr:
            for i in s:
                x=ast.literal_eval(i)
                if x["reg_no"] == reg_no:
                    list.append("1")
                    marks = x["marks"]

                    total = sum(marks)
                    average = total / 3

                    if all(mark >= 40 for mark in marks):
                        status = "Pass"
                    else:
                        status = "Fail"
                    if list!=[]:
                        print("\nRegistration Number:", x["reg_no"])
                        print("Department:", x["department"])
                        print("Name:", x["name"])
                        print("Total Marks:", total)
                        print("Average Marks:", average)
                        print("Status:", status)

    if list==[]:
        print("student not found")


