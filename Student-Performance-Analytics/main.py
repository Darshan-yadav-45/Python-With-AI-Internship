
import pandas as pd

from functions import (
    load_student_data,
    process_student_data,
    get_class_summary,
    get_subject_analysis,
    get_top_performers,
    get_low_attendance_students
)


def display_heading(title):
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def main():
    try:
        # Load student dataset
        students = load_student_data("students.csv")

        # Process marks, averages, grades and results
        students = process_student_data(students)

        display_heading("STUDENT PERFORMANCE ANALYTICS SYSTEM")

        print(f"\nTotal records loaded: {len(students)}")

        # Display dataset information
        display_heading("STUDENT DATA")
        print(students.head(10).to_string(index=False))

        print("\nDataset shape:", students.shape)
        print("\nDataset information:")
        print(students.info())

        # Individual student performance
        display_heading("INDIVIDUAL STUDENT PERFORMANCE")
        print(
            students[
                [
                    "Student_ID",
                    "Name",
                    "Total_Marks",
                    "Average_Marks",
                    "Grade",
                    "Result"
                ]
            ].to_string(index=False)
        )

        # Class summary
        display_heading("CLASS PERFORMANCE SUMMARY")
        summary = get_class_summary(students)

        for label, value in summary.items():
            print(f"{label:<25}: {value}")

        # Subject analysis
        display_heading("SUBJECT-WISE PERFORMANCE")
        subject_analysis = get_subject_analysis(students)
        print(subject_analysis.to_string(index=False))

        best_subject = subject_analysis.loc[
            subject_analysis["Average Marks"].idxmax()
        ]

        print(
            f"\nBest-performing subject: {best_subject['Subject']}"
        )
        print(
            f"Subject average: {best_subject['Average Marks']}"
        )

        # Top five performers
        display_heading("TOP 5 PERFORMING STUDENTS")
        top_students = get_top_performers(students, 5)
        print(top_students.to_string(index=False))

        # Lowest-performing students
        display_heading("BOTTOM 5 STUDENTS BY AVERAGE")
        bottom_students = students.nsmallest(
            5, "Average_Marks"
        )[
            [
                "Student_ID",
                "Name",
                "Average_Marks",
                "Grade",
                "Result"
            ]
        ]
        print(bottom_students.to_string(index=False))

        # Attendance analysis
        display_heading("LOW ATTENDANCE STUDENTS")
        low_attendance = get_low_attendance_students(students)

        if low_attendance.empty:
            print("All students have attendance of at least 75%.")
        else:
            print(low_attendance.to_string(index=False))

        # Save analyzed results as a CSV file is not required;
        # all results are displayed directly in the console.

        display_heading("ANALYSIS COMPLETED SUCCESSFULLY")

    except FileNotFoundError:
        print(
            "Error: students.csv was not found. "
            "Place it in the project folder."
        )
    except (ValueError, KeyError) as error:
        print(f"Data validation error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
