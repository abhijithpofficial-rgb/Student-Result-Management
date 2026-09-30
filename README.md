# Student Result Management System

The Student Result Management System is a Python-based application designed to manage student academic records efficiently. The system allows users to add, search, display, and delete student information through a simple menu-driven interface.

---

##  Features

* **Add Student**: Register new students with unique registration numbers, personal details, and marks for three subjects. Prevent duplicate registrations.
* **Search Student**: Quickly locate specific student details using their unique registration number.
* **Display Result**: Calculate and view total marks, percentage/average, and pass/fail status based on standard grading thresholds (minimum 40 marks per subject).
* **Display All Records**: List complete academic information for all students saved in the system.
* **Delete Record**: Remove student records by registration number.
* **CSV Data Persistence**: Stores all student records locally in `student.csv`.

---

##  Project Structure

```text
├── main.py          # Application entry point containing the main interactive menu loop
├── student_add.py   # Handles adding new student records and duplicate checks
├── search.py        # Logic to search for specific students by registration number
├── display.py       # Displays detailed results, averages, and pass/fail status for a student
├── displayall.py    # Displays all student records stored in the system
├── delete.py        # Module for removing a student record from the CSV file
└── student.csv      # CSV database file where records are stored (automatically generated/updated)
```

---

##  Getting Started

### Prerequisites

* Python 3.x installed on your computer.

### Running the Application

1. Open your terminal or command prompt in the project directory.
2. Run `main.py` using Python:

```bash
python main.py
```

---

##  Main Menu Options

```text
┌──────────────────────────────────────────────────────────┐
│                         MAIN MENU                        │
├──────────────────────────────────────────────────────────┤
│  1.  Add Student                                         │
│  2.  Search Student                                      │
│  3.  Display Student Result                              │
│  4.  Display All Students                                │
│  5.  Delete                                              │
│  6.  Exit                                                │
└──────────────────────────────────────────────────────────┘
```

1. **Add Student**: Input registration number, name, department, and marks for 3 subjects.
2. **Search Student**: Retrieve basic details for a student.
3. **Display Student Result**: View calculated totals, average marks, and overall status (`Pass` if all subjects $\ge 40$, otherwise `Fail`).
4. **Display All Students**: List all current students in the database.
5. **Delete**: Enter registration number to remove a record.
6. **Exit**: Terminate the application.

## Conclusion
The Student Result Management System provides an efficient, lightweight command-line solution for managing student academic records. Built using Python's native modules (csv, ast, and os), it offers key database functionalities—including addition, lookup, result computation, display, and deletion—without requiring external database engines.
