import numpy as np

rnd = np.random.default_rng(seed=10)

min_mark = 0
max_mark = 100
no_of_students = 500
no_of_subjects = 5

student_marks = rnd.integers(min_mark,max_mark+1,size=(no_of_students,no_of_subjects))
average_marks = student_marks.mean(axis=1)
subject_average = student_marks.mean(axis=0)