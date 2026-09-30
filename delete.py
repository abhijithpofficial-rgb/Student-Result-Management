import csv
import ast
import os
def delete_student():
    list = []
    with open("student.csv",'r') as stud:
        cr=csv.reader(stud)
        reg_no = input("Enter Registration Number: ")
        if os.path.getsize("student.csv")==0:

            print("No records found")
            return
        for s in cr:
            for i in s:
                list.append(ast.literal_eval(i))
    list1=[]
    list2=[]
    for s in list:
        if s["reg_no"] != reg_no:
            list1.append(s)
            list2.append(s["reg_no"])
        else:
            list2.append(s["reg_no"])

    if reg_no not in list2 and list2!= []:
        print("enter a valid register number")

    with open("student.csv",'w',newline='') as stu:
        cw=csv.writer(stu)
        if list1!=[]:
            cw.writerow(list1)
'''delete_student()'''