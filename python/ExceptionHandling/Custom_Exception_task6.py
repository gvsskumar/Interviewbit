# Write a function that processes student marks and raises a Custom GradeException if marks are greater than 100. 
# Custom Exception
class GradeException(Exception):
    pass


def process_marks(marks):
    if marks > 100:
        raise GradeException("Marks cannot be greater than 100.")
    else:
        print("Student Marks:", marks)


try:
    student_marks = int(input("Enter student marks: "))
    process_marks(student_marks)

except GradeException as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a numeric value.")

finally:
    print("Program execution completed.")
    