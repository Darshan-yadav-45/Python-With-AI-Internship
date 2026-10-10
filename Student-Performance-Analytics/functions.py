
import numpy as np
import pandas as pd


SUBJECTS = [
    "Python_Marks",
    "Mathematics_Marks",
    "Database_Marks",
    "Computer_Networks_Marks"
]

PASS_MARKS = 40
MIN_ATTENDANCE = 75


def load_student_data(file_path="students.csv"):
    """Load and validate student data from a CSV file."""
    df = pd.read_csv(file_path)

    required_columns = [
        "Student_ID",
        "Name",
        "Department",
        *SUBJECTS,
        "Attendance_Percentage"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("The student dataset is empty.")

    if df[required_columns].isnull().any().any():
        raise ValueError("The dataset contains missing values.")

    for subject in SUBJECTS:
        df[subject] = pd.to_numeric(
            df[subject], errors="raise"
        )

        if not df[subject].between(0, 100).all():
            raise ValueError(
                f"{subject} must contain marks between 0 and 100."
            )

    df["Attendance_Percentage"] = pd.to_numeric(
        df["Attendance_Percentage"], errors="raise"
    )

    if not df["Attendance_Percentage"].between(0, 100).all():
        raise ValueError(
            "Attendance must be between 0 and 100."
        )

    return df


def calculate_total_marks(df):
    """Calculate total marks across all subjects."""
    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    return df


def calculate_average_marks(df):
    """Calculate average marks across all subjects using NumPy."""
    marks_array = df[SUBJECTS].to_numpy(dtype=float)

    df["Average_Marks"] = np.round(
        np.mean(marks_array, axis=1), 2
    )

    return df


def assign_grade(average):
    """Assign a grade based on the student's average."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def assign_grades(df):
    """Assign grades to all students."""
    df["Grade"] = df["Average_Marks"].apply(assign_grade)
    return df


def assign_pass_fail(df):
    """
    Pass criteria:
    At least 40 marks in every subject and attendance
    of at least 75 percent.
    """
    subject_pass = (df[SUBJECTS] >= PASS_MARKS).all(axis=1)
    attendance_pass = (
        df["Attendance_Percentage"] >= MIN_ATTENDANCE
    )

    df["Result"] = np.where(
        subject_pass & attendance_pass,
        "Pass",
        "Fail"
    )

    return df


def get_class_summary(df):
    """Return overall class performance statistics."""
    total_students = len(df)
    passed_students = int((df["Result"] == "Pass").sum())
    failed_students = int((df["Result"] == "Fail").sum())

    pass_percentage = (
        passed_students / total_students * 100
        if total_students else 0
    )

    return {
        "Total Students": total_students,
        "Class Average": round(df["Average_Marks"].mean(), 2),
        "Highest Average": round(df["Average_Marks"].max(), 2),
        "Lowest Average": round(df["Average_Marks"].min(), 2),
        "Passed Students": passed_students,
        "Failed Students": failed_students,
        "Pass Percentage": round(pass_percentage, 2),
        "Average Attendance": round(
            df["Attendance_Percentage"].mean(), 2
        )
    }


def get_subject_analysis(df):
    """Calculate average, highest, and lowest marks per subject."""
    analysis = []

    for subject in SUBJECTS:
        marks = df[subject].to_numpy(dtype=float)

        analysis.append({
            "Subject": subject.replace("_Marks", "").replace("_", " "),
            "Average Marks": round(float(np.mean(marks)), 2),
            "Highest Marks": int(np.max(marks)),
            "Lowest Marks": int(np.min(marks)),
            "Students Passed": int((marks >= PASS_MARKS).sum()),
            "Students Failed": int((marks < PASS_MARKS).sum())
        })

    return pd.DataFrame(analysis)


def get_top_performers(df, count=5):
    """Return the top students ranked by average marks."""
    return df.nlargest(count, "Average_Marks")[
        [
            "Student_ID",
            "Name",
            "Department",
            "Average_Marks",
            "Grade",
            "Result"
        ]
    ]


def get_low_attendance_students(df):
    """Find students whose attendance is below 75 percent."""
    return df[
        df["Attendance_Percentage"] < MIN_ATTENDANCE
    ][
        ["Student_ID", "Name", "Attendance_Percentage"]
    ]


def process_student_data(df):
    """Run all student calculations in the correct order."""
    df = df.copy()
    df = calculate_total_marks(df)
    df = calculate_average_marks(df)
    df = assign_grades(df)
    df = assign_pass_fail(df)
    return df
