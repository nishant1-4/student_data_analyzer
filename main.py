import numpy as np

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
