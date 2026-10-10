
# STUDENT PERFORMANCE ANALYTICS SYSTEM

## Project Documentation

**Student Name:** Darshan K M  
**College Name:** CMR University, Bengaluru  
**Programme:** Master of Computer Applications (MCA)  
**Course:** Python with AI  
**Project Title:** Student Performance Analytics System  
**Technologies Used:** Python, NumPy, Pandas  
**Dataset File:** students.csv  

---

## 1. Project Title

Student Performance Analytics System

## 2. Objective

The objective of this project is to develop a Python-based
Student Performance Analytics System that processes and analyzes
student marks and attendance.

The system calculates total marks, average marks, grades, and
pass/fail results. It also analyzes overall class performance,
subject-wise performance, top-performing students, and attendance.

This project demonstrates the practical use of Python programming,
NumPy, and Pandas to organize student data, perform calculations,
and generate meaningful analytical results.

## 3. Technologies Used

### 3.1 Python

Python is used to implement the program logic, variables, data types,
conditional statements, loops, and reusable functions. It also
controls the processing and display of analytical results.

### 3.2 NumPy

NumPy is used for numerical computations, including calculating
student averages and performing subject-wise statistical analysis.

### 3.3 Pandas

Pandas is used to read the CSV dataset into a DataFrame, organize
student records, calculate total marks, filter records, sort data,
and analyze student performance.

### 3.4 CSV

CSV is the file format used to store student details, subject marks,
and attendance in a structured tabular format.

## 4. Dataset Description

The project uses a dataset stored in `students.csv`.

The dataset contains the following fields:

| Column Name | Description |
|---|---|
| Student_ID | Unique identifier for each student |
| Name | Name of the student |
| Department | Department of the student |
| Python_Marks | Marks obtained in Python |
| Mathematics_Marks | Marks obtained in Mathematics |
| Database_Marks | Marks obtained in Database |
| Computer_Networks_Marks | Marks obtained in Computer Networks |
| Attendance_Percentage | Student attendance percentage |

Each subject is evaluated out of 100 marks. Attendance is represented
as a percentage between 0 and 100.

**Dataset Size:** 500 student records, when the completed
500-record dataset is included.

The dataset is used to calculate individual student results and
analyze overall academic performance.

## 5. Implementation

### 5.1 Prepare the Dataset

Student information, subject marks, and attendance are stored in
the `students.csv` file. The dataset contains column headings so
that the records can be loaded and processed using Pandas.

### 5.2 Load the Dataset

The Pandas `read_csv()` function loads the CSV file into a DataFrame.
The program checks the required columns and validates marks,
attendance, and missing values.

### 5.3 Calculate Total Marks

The program adds the marks obtained in all four subjects to calculate
the total marks for each student.

**Formula:**

Total Marks = Python + Mathematics + Database + Computer Networks

The calculation is performed using Pandas DataFrame operations.

### 5.4 Calculate Average Marks

The average marks represent the student's average performance
across the four subjects.

**Formula:**

Average Marks = Total Marks / Number of Subjects

NumPy is used to calculate numerical averages.

### 5.5 Assign Grades

Grades are assigned according to the student's average marks.

| Average Marks | Grade |
|---|---|
| 90 to 100 | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

Conditional statements are used to assign the appropriate grade.

### 5.6 Determine Pass or Fail

The project uses the following passing criteria:

- The student must score at least 40 marks in every subject.
- The student must have attendance of at least 75%.

A student who satisfies both conditions is classified as Pass.
Otherwise, the student is classified as Fail.

### 5.7 Analyze Class Performance

The system calculates the following class statistics:

- Total number of students
- Overall class average
- Highest student average
- Lowest student average
- Number of passed students
- Number of failed students
- Pass percentage
- Average attendance

The results provide an overview of the academic performance
of the students in the dataset.

### 5.8 Perform Subject-Wise Analysis

The system analyzes each subject separately and calculates:

- Average marks
- Highest marks
- Lowest marks
- Number of students passing the subject
- Number of students failing the subject

The subject with the highest average marks is identified as
the best-performing subject.

### 5.9 Identify Top Performers

The system identifies the top five students based on their
average marks.

It also displays the five students with the lowest average marks
to help compare student performance.

Pandas sorting and ranking operations are used for this analysis.

### 5.10 Analyze Attendance

The program calculates average attendance and identifies students
whose attendance is below 75%.

This helps identify students who do not meet the attendance
criterion used in the project.

### 5.11 Display the Results

The main program displays:

- Student records
- Total and average marks
- Grades and pass/fail status
- Class performance statistics
- Subject-wise analysis
- Top five performers
- Five lowest-performing students
- Students with low attendance

The results are displayed in the terminal in a readable format.

## 6. Key Features

1. Reads student data from a CSV file.
2. Organizes records using a Pandas DataFrame.
3. Calculates total and average marks.
4. Assigns grades using conditional statements.
5. Determines pass/fail results using marks and attendance.
6. Calculates overall class performance statistics.
7. Performs subject-wise performance analysis.
8. Identifies the top five performing students.
9. Identifies the five students with the lowest averages.
10. Finds students with attendance below 75%.
11. Uses reusable functions for calculations and processing.
12. Uses NumPy for numerical computations.
13. Uses Pandas for data loading, filtering, sorting, and analysis.

## 7. Output and Screenshots

The program produces analytical results based on the student dataset.

The expected output includes:

- Student dataset preview
- Individual student performance
- Class performance summary
- Subject-wise performance table
- Best-performing subject
- Top five performing students
- Five students with the lowest averages
- Low-attendance student list

### Screenshots

Screenshots of the actual program output can be added to the
project repository to demonstrate successful execution.

Recommended screenshots:

1. Student dataset and individual performance
2. Class performance summary
3. Subject-wise performance analysis
4. Top performers and attendance analysis

Only screenshots captured from the tested program should be
included as actual project results.

## 8. Final Outcome

The Student Performance Analytics System successfully demonstrates
how Python, NumPy, and Pandas can be used to process and analyze
structured student data.

The system calculates marks, averages, grades, and pass/fail
results. It also summarizes class performance, analyzes individual
subjects, identifies top-performing students, and finds students
with low attendance.

The project provides practical experience in Python programming
fundamentals and data analysis.

## 9. Challenges and Learning Outcomes

### 9.1 Challenges

Potential challenges during development include:

- Loading and organizing CSV data correctly.
- Handling missing or invalid data.
- Implementing grading conditions accurately.
- Applying pass/fail criteria consistently.
- Performing numerical calculations correctly.
- Filtering student records and identifying top performers.
- Presenting analytical results in a readable format.

### 9.2 Learning Outcomes

Through this project, I gained practical experience in:

- Python variables and data types.
- Conditional statements and loops.
- Creating and using reusable functions.
- Reading and processing CSV files.
- Creating and manipulating Pandas DataFrames.
- Performing numerical computations using NumPy.
- Filtering, sorting, and summarizing datasets.
- Analyzing student marks and attendance.
- Interpreting statistical results.
- Organizing project files and maintaining a GitHub repository.

Update the challenges section with the actual problems encountered
during development and the solutions used.

## 10. GitHub Repository

**Repository Name:** Student-Performance-Analytics

**Repository URL:**  
Add the actual GitHub repository URL after uploading the project.

The repository contains the Python source files, student dataset,
README, and project documentation.

## Conclusion

The Student Performance Analytics System demonstrates the
application of Python programming fundamentals, NumPy, and Pandas
to student data analysis.

It provides meaningful summaries of student marks, grades,
class performance, subject-wise results, and attendance.

The project reinforces programming concepts, numerical
computations, data processing, and analytical problem-solving.

---

**Submitted by:** Darshan K M  
**Institution:** CMR University, Bengaluru  
**Programme:** Master of Computer Applications (MCA)  
**Course:** Python with AI
