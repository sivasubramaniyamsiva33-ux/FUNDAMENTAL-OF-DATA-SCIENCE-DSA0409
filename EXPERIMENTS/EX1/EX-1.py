import numpy as np

student_scores = np.array([
    [80, 75, 85, 70],
    [90, 85, 80, 75],
    [70, 80, 90, 85],
    [85, 90, 95, 80]
])

subjects = ["Math", "Science", "English", "History"]

average = np.mean(student_scores, axis=0)

for i in range(4):
    print(subjects[i], "Average =", average[i])

highest = np.argmax(average)
print("Highest average subject:", subjects[highest])
