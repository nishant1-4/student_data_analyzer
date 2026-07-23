import numpy as np
import pathlib as pth

rnd = np.random.default_rng(seed=10)

min_mark = 0
max_mark = 100
no_of_students = 500
no_of_subjects = 5
subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]

student_marks = rnd.integers(
    min_mark, max_mark + 1, size=(no_of_students, no_of_subjects)
)
average_marks = student_marks.mean(axis=1)
subject_average = student_marks.mean(axis=0)
topper_index = average_marks.argmax()


def total_average_per_subject(arr):
    for count, marks in enumerate(arr):
        print(f"{subjects[count]} -> {marks}")


def details_of_topper(subject_arr, marks_arr, avg_arr, topper_index):
    print(
        f"Student no. {topper_index+1} is the topper of the class.\nAverage -> {avg_arr[topper_index]}\n"
    )

    for subject, marks in zip(subject_arr, marks_arr[topper_index]):
        print(f"{subject} -> {marks}")


def top_n_students(avg_mark: np.ndarray, top_n: int):
    top_list = avg_mark.argsort()[-(top_n):][::-1]
    count = 1
    for student, avg in zip(top_list, avg_mark[top_list]):
        print(f"{count}. Student {student+1} -> {avg}")
        count += 1


def assign_grade(avg_mark, need_grades: bool = False):
    conditions = [
        (avg_mark >= 90),
        (avg_mark >= 80) & (avg_mark < 90),
        (avg_mark >= 70) & (avg_mark < 80),
        (avg_mark >= 60) & (avg_mark < 70),
        (avg_mark >= 50) & (avg_mark < 60),
        (avg_mark < 50),
    ]
    choice = [chr(i) for i in range(65, 71)]  # ['A','B','C','D','E','F']
    grades_arr = np.select(conditions, choice, default="Invalid")
    return grades_arr


def grades_distribution(grades):
    grade, number_of_grades = np.unique(grades, return_counts=True)
    print("Number of students in each grade:")
    for gr, num in zip(grade, number_of_grades):
        print(f"{gr}: {num}")


def failed_students(grades):
    failed_students = np.where(grades == "F")[0]
    print(f"Total {failed_students.size} has failed!")
    for student in failed_students:
        print(f"Student {student+1}")


def save_students_data(file_name, **data):
    if pth.Path(file_name).is_file():
        choice = input(
            f"The file {file_name} already exists, do you want to override? (y/any key to cancel): "
        )
        if not choice == "y":
            print("Operation cancelled!")
            return
    np.savez(file_name, **data)
    print("Data saved successfully")


def load_student_data(file_name):
    try:
        data = np.load(file_name)
        print("Data fetched successfully")
        return data
    except Exception as e:
        print(f"File not found\n{e}")


save_students_data("student_data.npz", student_marks=student_marks)
