# Problem & Scope Statement

## 1. Problem Statement
Educational institutions and instructors often need a simple, lightweight, and offline method to manage student academic records, perform pass/fail calculations, and search or delete records as needed. Manual record-keeping in spreadsheets or paper logs is prone to human error, loss of data integrity, and inefficient searching. Existing heavy database systems or enterprise software can be overly complex and resource-intensive for small-scale administrative tasks or local usage. There is a need for a streamlined, command-line interface (CLI) application that securely processes student marks, computes performance metrics automatically, and maintains simple file-based persistence.

## 2. Scope of the Project
The **Student Result Management System** is a terminal-based utility developed in Python using standard libraries (`csv`, `ast`, and `os`).

### What is In Scope:
* **CRUD Operations**: Creation (Add student), Reading (Search and Display), and Deletion (Remove student record) of student academic data.
* **Result Calculation**: Automated computing of total marks, average scores across three subjects, and Pass/Fail evaluation based on a minimum threshold (40 marks per subject).
* **Data Validation**: Prevention of duplicate registration numbers during record creation.
* **File-Based Persistence**: Storing records locally in standard CSV format (`student.csv`).

### What is Out of Scope:
* Multi-user authentication, roles (e.g., student vs. admin access), or security encryption.
* Advanced reporting features (e.g., PDF generation, class rankings, grade point averages / GPA scaling).
* Graphical User Interface (GUI) or web accessibility.
* Handling subjects beyond the hardcoded 3-subject format.

## 3. Target Users
* **Educators & Tutors**: Individual teachers or small-scale tutors who need a fast, low-overhead program to maintain student marks and print/view quick status summaries.
* **Academic Administrators**: Staff handling small departments or batches who require offline tools for student record maintenance without complex software setups.
* **Students/Learners**: Beginners studying Python development, file operations, and CLI menu architectures.

## 4. High-Level Features
* **Interactive CLI Main Menu**: Clear text interface providing intuitive menu-driven navigation for options 1–6.
* **Duplicate Prevention**: Active check against existing registration numbers before committing new student data to storage.
* **Automated Result Computation Engine**:
  * Summation of subject scores ($\text{Total} = m_1 + m_2 + m_3$).
  * Calculation of average score ($\text{Average} = \frac{\text{Total}}{3}$).
  * Rule-based status assignment (`Pass` if $m_i \ge 40$ for all subjects, otherwise `Fail`).
* **Individual Record Search & Result Display**: Quick lookup by unique registration number displaying full profile details and calculated performance.
* **Batch Display**: Comprehensive overview displaying calculated stats for all enrolled students in one view.
* **Record Deletion**: Efficient removal of student entries from the CSV file matching a target registration number.