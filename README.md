This project implements a student grading and pass/fail determination system. Here's what it does:

Reads student data line by line from a file named data.txt. Each line contains: student name, 6 quiz scores, 4 task scores, one midterm exam score, and one final exam score.

For each student:

Drops the two lowest quiz scores and averages the remaining four.

Drops the lowest task score and averages the remaining three.

Calculates final grade = (average quiz + average task + midterm + final) / 4.

If final grade ≥ 60 → "pass", otherwise → "fail".

Finally, prints a dictionary with student names and their pass/fail status.
