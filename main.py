from student_add import add_student
from display import display_result
from search import search_student
from displayall import display_all_students
from delete import delete_student
y='yes'
while y=='yes':
    print("┌──────────────────────────────────────────────────────────┐")
    print(
        "│                         MAIN MENU                        │")
    print("├──────────────────────────────────────────────────────────┤")
    print(
        "│  1.  Add Student                                         │")
    print(
        "│  2.  Search Student                                      │")
    print(
        "│  3.  Display Student Result                              │")
    print(
        "│  4.  Display All Students                                │")
    print(
        "│  5.  Delete                                              │")
    print(
        "|  6.  Exit                                                │")
    print("└──────────────────────────────────────────────────────────┘")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        display_result()

    elif choice == "4":
        display_all_students()

    elif choice=="5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Result Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
    x=input("enter yes for continue : ")
    y=x.lower()