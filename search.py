import csv
import ast
def search_student():
    regno = input("Enter Registration Number: ")
    l=[]
    with open('student.csv','r') as stud:
        cr=csv.reader(stud)
        for s in cr:
            for i in s:
                x=ast.literal_eval(i)
                if x['reg_no'] == regno:
                    print("Registration Number:", x["reg_no"])
                    print("Name:", x["name"])
                    print("Department:", x["department"])
                    print("Marks:", x["marks"])
                    l.append("1")
                    break
        if l==[]:
            print("Student not found.")