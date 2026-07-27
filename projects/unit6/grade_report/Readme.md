# Unit 6 Practical task – Grade Report

## Overview
Create a Python script called `grade_report.py` that processes a list of student dictionaries, generates a grade and status for each student, and produces a full class summary report.  
The program demonstrates loops, conditional logic, data structures, and formatted output.

---

## Requirements
- Store at least 5 students as a list of dictionaries:  
  `[{name, maths, english, science}, …]`
- Use a `for` loop to iterate over all students and calculate each student’s average.
- Apply the grade/status logic from Unit 5 inside the loop:
  - A → 80+
  - B → 70–79
  - C → 60–69
  - D → 50–59
  - F → below 50
  - Pass → average ≥ 50
  - Fail → average < 50
- Build a results list of dictionaries containing:
  - `name`, `average`, `grade`, `status`
- After the main loop, calculate:
  - Class average
  - Highest mark
  - Lowest mark
- Display a formatted class report showing:
  - Individual student results
  - Class statistics
- Use a `while` loop to let the user search for a student by name after the report is shown.

---

## Outcome
By completing this task, you will:
- Understand how to store and process structured data with lists and dictionaries.
- Apply conditional logic to classify grades and status.
- Generate both individual and class-level statistics.
- Use loops to automate repetitive tasks and enable searching.
- Build confidence in combining input, conditionals, loops, and formatted output in a single program.
