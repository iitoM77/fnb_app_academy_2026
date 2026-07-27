# Unit 4 Practical task – Student Grade Classifier

## Overview
Create a Python script called `grade_classifier.py` that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card.  
The program demonstrates conditional logic, arithmetic operations, and formatted output.

---

## Requirements
- Collect learner name and marks for three subjects (as floats) using `input()`.
- Calculate the average mark across the three subjects.
- Assign a letter grade using `if/elif/else`:
  - A → 80+
  - B → 70–79
  - C → 60–69
  - D → 50–59
  - F → below 50
- Assign status:
  - Pass → average ≥ 50
  - Fail → average < 50
- Flag any individual subject mark below 40 as **needs intervention**.
- Display a formatted report card showing:
  - Learner name
  - Subject marks
  - Average
  - Grade
  - Status
  - Intervention flags (if any)

---

## Outcome
By completing this task, you will:
- Understand how to collect and process multiple numeric inputs.
- Apply conditional logic to classify grades and status.
- Detect and flag weak subject performance.
- Use f-strings to display a clear, formatted report card.
- Build confidence in combining input, calculation, conditionals, and output in a single program.
