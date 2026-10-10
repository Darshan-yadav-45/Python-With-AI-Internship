
# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based data analysis
program that processes student marks and attendance using NumPy and Pandas.

It calculates student totals, averages, grades, pass/fail results,
class statistics, subject-wise performance, and top-performing students.

## Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset

## Features
- Load student records from a CSV file.
- Calculate total and average marks.
- Assign grades based on average marks.
- Determine pass/fail status.
- Calculate class performance statistics.
- Analyze subject-wise marks.
- Identify top five performers.
- Find students with attendance below 75%.

## Project Structure
- `main.py` - Main program.
- `functions.py` - Reusable calculation and analysis functions.
- `students.csv` - Student dataset.
- `README.md` - Project overview.
- `Project_Documentation.md` - Detailed documentation.

## Installation
Install Python, then install the required libraries:

```bash
python -m pip install numpy pandas
```

## How to Run
1. Keep `main.py`, `functions.py`, and `students.csv` in the same folder.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

## Grading Rules
- A+ : Average of 90 or above
- A  : Average of 80 to below 90
- B  : Average of 70 to below 80
- C  : Average of 60 to below 70
- D  : Average of 50 to below 60
- F  : Average below 50

## Passing Criteria
A student passes only if they score at least 40 marks in every
subject and have attendance of at least 75%.

## Learning Outcomes
This project demonstrates Python variables, data types, conditions,
loops, functions, NumPy numerical operations, Pandas DataFrames,
CSV handling, and data analysis.
