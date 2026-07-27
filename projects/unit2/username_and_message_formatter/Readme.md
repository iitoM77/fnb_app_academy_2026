# Project 3 – Username and Message Formatter

##  Overview
Create a Python script called `string_formatter.py` that collects a user’s first name, last name, and a short bio message, then applies multiple string transformations to produce a formatted user profile output.  
This project simulates how a real app backend processes user-submitted text.

---

## Requirements
- Collect input using `input()`:
  - First name
  - Last name
  - Bio message

- Create a username:
  - Combine first initial + last name in lowercase

- Display the full name:
  - Use `.title()` for Title Case

- Format the bio:
  - Strip leading/trailing whitespace using `.strip()`
  - Count and display characters using `len()`
  - Replace `"I am"` with `"I'm"` using `.replace()`

- Display all output using **f-strings**

---

## Outcome
By completing this task, you will:
- Understand how to collect and process multiple user inputs.
- Apply string methods to transform and clean text.
- Generate usernames programmatically.
- Use f-strings for clear, formatted output.
- Build confidence in simulating real-world text processing tasks.
