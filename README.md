# Student Performance Analyzer

A beginner-friendly Python project built with **NumPy** to practice array manipulation, statistical analysis, sorting, filtering, and file handling.

This project simulates the academic performance of **500 students** across **5 subjects** and analyzes the generated data using various NumPy operations. It was created as part of my AI/ML engineering learning journey to strengthen my NumPy fundamentals before moving on to Pandas and Machine Learning.

---

## Features

* Generate random marks for 500 students
* Calculate average marks for each student
* Calculate average marks for each subject
* Find the class topper
* Display the Top N students based on average marks
* Assign grades (A–F) based on average scores
* Display grade distribution
* Identify failed students
* Save and load project data using NumPy (`.npz` format)

---

## Technologies Used

* Python 3
* NumPy

---

## Project Structure

```text
student-performance-analyzer/
│
├── main.py
├── README.md
└── .gitignore
```

---

## NumPy Concepts Practiced

This project covers the following NumPy concepts:

* Random number generation
* Multi-dimensional arrays
* Array indexing and slicing
* Statistical operations (`mean`)
* Finding maximum values (`argmax`)
* Sorting indices (`argsort`)
* Boolean masking
* Conditional selection using `np.select()`
* Counting unique values using `np.unique()`
* Saving and loading data using `np.savez()` and `np.load()`

---

## Example Output

```text
Student Averages
----------------
Student 1 : 74.60
Student 2 : 81.20
...

Subject Averages
----------------
Math       : 72.45
Physics    : 69.81
Chemistry  : 71.30
English    : 73.12
Computer   : 70.94

Topper
------
Student 237
Average : 96.80

Top 5 Students
--------------
1. Student 237 -> 96.80
2. Student 182 -> 95.40
3. Student 419 -> 95.20
4. Student 301 -> 94.60
5. Student 125 -> 94.20

Grade Distribution
------------------
A : 48
B : 116
C : 172
D : 104
E : 38
F : 22
```

---

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project directory

```bash
cd student-performance-analyzer
```

### Install NumPy

```bash
pip install numpy
```

### Run the project

```bash
python main.py
```

---

## Learning Outcomes

By building this project, I practiced:

* Writing modular Python code
* Applying NumPy to solve data analysis problems
* Working with multidimensional arrays
* Performing statistical analysis
* Ranking and filtering data efficiently
* Saving and loading datasets
* Structuring a small Python project
* Using Git for version control throughout development

---

## Future Improvements

* Read student data from CSV files using Pandas
* Add visualizations with Matplotlib and Seaborn
* Build a command-line interface (CLI)
* Store data in a database
* Apply machine learning models to predict student performance

---

## Author

Developed as part of my AI/ML engineering learning journey to build a strong foundation in NumPy before progressing to Pandas.