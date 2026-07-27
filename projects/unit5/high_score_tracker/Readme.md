# Unit 5 Challenge – High Score Tracker

## Overview
Create a Python script called `high_score_tracker.py` that continuously asks an arcade player for their game score and provides feedback.  
The program demonstrates infinite loops, input handling, conditional logic, and formatted output.

---

## Requirements
1. Start an intentional infinite loop using `while True:`.
2. Inside the loop, ask the user to enter a game score.
3. If the user types `"stop"`:
   - Clean the input with `.strip().lower()`.
   - Print: `Game session ended!`
   - Use `break` to exit the loop.
4. Otherwise:
   - Cast the input into an integer.
   - Check if the score is greater than 100.
   - Print either:
     - `"Wow! That’s a new high score!"`  
     - `"Good try, keep playing!"` based on the value.

---

## Outcome
By completing this task, you will:
- Understand how to use infinite loops with `while True`.
- Safely handle user input with string methods and type casting.
- Apply conditional logic to provide dynamic feedback.
- Use `break` to exit loops when a condition is met.
- Build confidence in combining loops, conditionals, and formatted output in interactive programs.
