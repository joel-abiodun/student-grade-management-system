# Student Grade Management System
# Author: Joel Abiodun
# Matric Number: 25/18070
# Department: Computer Science
# Institution: Caleb University

def calculate_total_score(test_score, exam_score):
    """
    This function calculates the total score
    by adding test score and exam score.
    """
    return test_score + exam_score


def assign_grade(total_score):
    """
    This function assigns a grade based on the total score.
    """
    if total_score >= 70:
        return "A"
    elif total_score >= 60:
        return "B"
    elif total_score >= 50:
        return "C"
    elif total_score >= 45:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Management System =====")

    # Collect student details
    student_name = input("Enter student name: ")

    test_score = float(input("Enter test score (out of 30): "))
    exam_score = float(input("Enter exam score (out of 70): "))

    # Calculate total score
    total_score = calculate_total_score(test_score, exam_score)

    # Assign grade
    grade = assign_grade(total_score)

    # Display result
    print("\n----- Student Result -----")
    print("Student Name:", student_name)
    print("Test Score:", test_score)
    print("Exam Score:", exam_score)
    print("Total Score:", total_score)
    print("Grade:", grade)
    print("--------------------------")


if __name__ == "__main__":
    main()
