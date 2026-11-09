# Student Performance Analytics System

## Project Introduction

The **Student Performance Analytics System** is a Python-based data analysis
program developed as the final project for the **EWB Courses – Python with AI
Internship**. It reads student records from a CSV file, processes marks and
attendance, and generates meaningful academic performance reports using
**NumPy** and **Pandas**.

---

## Project Objectives

- Load and validate student data from a CSV dataset.
- Calculate total marks and average marks for each student.
- Assign letter grades based on average marks.
- Determine pass or fail status using subject marks and attendance criteria.
- Summarise overall class performance.
- Perform subject-wise performance analysis.
- Identify top-performing and low-performing students.
- Identify students with attendance below the required threshold.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Program logic, loops, functions, conditionals |
| NumPy | Numerical computations (averages, statistics) |
| Pandas | CSV loading, DataFrame operations, filtering, sorting |
| CSV | Student dataset storage format |

---

## Project Structure

```
Student-Performance-Analytics/
├── main.py                   # Main program and final output
├── functions.py              # Reusable functions for all calculations
├── students.csv              # Dataset with exactly 50 student records
├── README.md                 # Project overview and execution instructions
├── Project_Documentation.md # Complete project documentation
└── screenshots/              # Actual output execution screenshots
    ├── 01_dataset_preview.png
    ├── 02_dataset_info.png
    ├── 03_individual_performance.png
    └── 04_summary_and_analysis.png
```

---

## Main Features

1. Load student records from `students.csv` using Pandas.
2. Display the full dataset and dataset information.
3. Calculate **total marks** and **average marks** per student.
4. Assign **grades** (A+, A, B, C, D, F) based on average marks.
5. Determine **Pass / Fail** status using marks and attendance.
6. Display **class performance summary** (class average, highest, lowest, pass%).
7. Perform **subject-wise analysis** (average, highest, lowest, pass/fail counts).
8. Identify the **best-performing subject**.
9. Display the **top 5 performing students**.
10. Display the **bottom 5 students** by average marks.
11. List all students with **attendance below 75%**.

---

## Dataset Description

- **File:** `students.csv`
- **Total Records:** 50 student records
- **Columns:**

| Column Name | Description |
|---|---|
| Student_ID | Unique identifier (STU001 – STU050) |
| Name | Student full name |
| Department | Academic department |
| Python_Marks | Marks in Python (0 – 100) |
| Mathematics_Marks | Marks in Mathematics (0 – 100) |
| Database_Marks | Marks in Database (0 – 100) |
| Computer_Networks_Marks | Marks in Computer Networks (0 – 100) |
| Attendance_Percentage | Attendance percentage (0 – 100) |

---

## Grading Rules

| Average Marks | Grade |
|---|---|
| 90 – 100 | A+ |
| 80 – below 90 | A |
| 70 – below 80 | B |
| 60 – below 70 | C |
| 50 – below 60 | D |
| Below 50 | F |

---

## Pass / Fail Criteria

A student **passes** only if they satisfy **both** conditions:

- Score **at least 40 marks** in every subject.
- Have **attendance of at least 75%**.

---

## Installation Instructions

Ensure Python is installed, then install the required libraries:

```bash
python -m pip install numpy pandas
```

---

## How to Run the Project

1. Place `main.py`, `functions.py`, and `students.csv` in the same folder.
2. Open a terminal and navigate to the project directory:

```bash
cd path/to/Student-Performance-Analytics
```

3. Run the program:

```bash
python main.py
```

---

## Expected Output

The program displays the following sections in the terminal:

- **Student Data** – Full dataset preview and dataset information.
- **Individual Student Performance** – Total marks, average, grade and result per student.
- **Class Performance Summary** – Class average, highest, lowest, pass/fail counts, pass%.
- **Subject-Wise Performance** – Average, highest, lowest marks and pass/fail per subject.
- **Best-Performing Subject** – Subject with the highest class average.
- **Top 5 Performing Students** – Ranked by average marks.
- **Bottom 5 Students** – Lowest average marks.
- **Low Attendance Students** – Students with attendance below 75%.

---

## GitHub Repository

**Repository URL:**  
[https://github.com/Darshan-yadav-45/Python-With-AI-Internship](https://github.com/Darshan-yadav-45/Python-With-AI-Internship)

---

## Student Information

| Field | Details |
|---|---|
| Student Name | Darshan K M |
| Institution | CMR University, Bengaluru |
| Programme | Master of Computer Applications (MCA) |
| Course | Python with AI |
| Email | darshan.km.091@gmail.com |
