# Python Notes – FNB App Academy

# Unit 1: Introduction to Python
## 1. What is Python?
- Python is a **high-level, interpreted programming language** (first released in 1991).
- Widely used in:
  - Data science → Netflix, Spotify
  - Web development → Instagram, Pinterest
  - Automation & scripting
  - Machine learning → Google, NASA
  - Mobile app development → via **Kivy framework**
- Syntax is designed to be **readable like plain English**, making it beginner-friendly yet powerful.

---

## 2. Your Development Environment
- Tools we use together:
  - **Python** → runs your code (the interpreter).
  - **Visual Studio Code (VS Code)** → where you write code (the editor).
- Setup steps:
  1. Install Python.
  2. Install VS Code.
  3. Add the **Microsoft Python extension** in VS Code.
     - Provides syntax highlighting, error detection, and run button.
  4. Create a folder called `app_academy` on your Desktop.
     - All programme work lives here.

---

## 3. Your First Script
- A **script** = plain text file with `.py` extension containing Python instructions.
- Fundamental instruction: `print()`
  - Displays a value to the terminal.
- Example:
  ```python
  print("Hello, world!")

---

# Unit 2 – Manipulating Strings

## 1. Why Strings Matter
- Strings are the most common data type in app development.
- Examples: usernames, messages, button labels, error messages, search results.
- Python provides built-in methods for transforming, searching, and formatting string data.
- Mastering string tools allows you to shape user input into the exact form your app needs.

---

## 2. String Methods
- A **method** is a built-in function that belongs to a specific data type.
- Called using **dot notation**: `variable.method()`
- Key string methods:
  - `.upper()` → converts to ALL CAPS
  - `.lower()` → converts to all lowercase
  - `.title()` → converts to Title Case
  - `.strip()` → removes leading and trailing whitespace
  - `.replace(old, new)` → swaps one substring for another
  - `.find(substring)` → returns index of first occurrence (`-1` if not found)
  - `.split(delimiter)` → breaks a string into a list
  - `len(string)` → returns character count

---

## 3. Indexing and Slicing
- Every character in a string has a position number called an **index**, starting at 0.
- Example: `name = "Python"`
  - `name[0]` → first character
  - `name[1]` → second character
  - `name[-1]` → last character
- **Slicing** extracts a portion:
  - `name[0:3]` → characters from index 0 up to (but not including) index 3
- Negative indexes count from the right:
  - `name[-3:]` → last three characters

---

## 4. f-Strings
- An **f-string** (formatted string literal) embeds variables and expressions inside text.
- Syntax: prefix string with `f` and wrap variables/expressions in `{}`.
- Example: `f"Welcome, {name.title()}!"`
- You can:
  - Call methods inside braces
  - Perform arithmetic
  - Embed any Python expression
- f-strings replace older styles like `.format()` and `%` formatting.
- Preferred style in modern Python.

---

# Unit 3 – Manipulating Numbers

## 1. Arithmetic Operators
- Python supports seven arithmetic operators:
  - Addition → `+`
  - Subtraction → `-`
  - Multiplication → `*`
  - Division → `/` (always returns a float, e.g. `10/2 = 5.0`)
  - Floor Division → `//` (discards the decimal, e.g. `10//3 = 3`)
  - Modulus → `%` (returns the remainder, e.g. `10%3 = 1`)
  - Exponentiation → `**` (raises to a power, e.g. `2**10 = 1024`)

---

## 2. The Type Casting Gotcha
- `input()` always returns a **string**.
- Common beginner error: trying to add a string and an integer → `TypeError`.
- Fix: wrap `input()` with `int()` or `float()`:
  - Use `int()` for whole numbers.
  - Use `float()` when decimals are possible.
- Always apply type casting when taking numeric input from a user.

---

## 3. Useful Number Functions
- `round(value, n)` → rounds to `n` decimal places.
- `abs(value)` → returns the absolute value (removes negative sign).
- `int()` → converts to integer.
- `float()` → converts to float.
- `str()` → converts to string.
- These are your main **type casting tools**.

---

## 4. Operator Precedence
- Python follows standard mathematical order of operations (**BEDMAS**):
  1. Brackets
  2. Exponents
  3. Division / Multiplication / Modulus
  4. Addition / Subtraction
- When in doubt, use brackets to make order explicit:
  - `(2 + 3) * 4 = 20`
  - `2 + 3 * 4 = 14` (multiplication happens first)

---

# Unit 4 – Storage and Access

## 1. Lists
- Ordered, mutable collection of values stored in a single variable.
- Create with square brackets: `students = ["Amara", "Sipho", "Lerato"]`
- Access items by index (starting at 0): `students[0]` → first item
- Negative indexes count from the end: `students[-1]` → last item
- Key methods:
  - `.append(item)` → adds to the end
  - `.insert(index, item)` → inserts at a position
  - `.remove(item)` → removes by value
  - `.pop(index)` → removes by index and returns the item
  - `len(list)` → returns the count

---

## 2. Dictionaries
- Store key–value pairs (lookup table).
- Create with curly braces: `contact = {"name": "Amara", "phone": "071 234 5678"}`
- Access values by key: `contact["name"]`
- Safe access: `.get("key")` → returns `None` if key doesn’t exist
- Key methods:
  - `.keys()` → all keys
  - `.values()` → all values
  - `.items()` → (key, value) pairs

---

## 3. Lists of Dictionaries
- Each dictionary represents one record (contact, student, product).
- The list holds all records together.
- Mirrors **database query results** and **API responses** (JSON).
- Iterate with a `for` loop to process every record.

---

## 4. Tuples – Immutable Lists
- Like lists but immutable (cannot be changed).
- Create with parentheses: `coordinates = (26.2, 28.0)`
- Use when data should not change:
  - GPS coordinates
  - RGB colour values
  - Days of the week
- Attempting to modify a tuple raises a `TypeError`.

---

# Unit 5 – Selection of Tasks

## 1. Conditional Logic
- `if / elif / else` let programs make decisions.
- Python checks conditions in order and executes the first block where condition is `True`.
- `elif` chains multiple conditions.
- `else` is the fallback block.
- **Indentation is mandatory**.

---

## 2. Comparison Operators
- Six operators return `True` or `False`:
  - `==` → equal to
  - `!=` → not equal to
  - `>` → greater than
  - `<` → less than
  - `>=` → greater than or equal to
  - `<=` → less than or equal to
-  Common bug: confusing assignment (`=`) with comparison (`==`).

---

## 3. Logical Operators
- Combine conditions:
  - `and` → both must be `True`
  - `or` → at least one must be `True`
  - `not` → inverts result
- Example: `if age >= 18 and has_id:` → entry granted only if both are `True`.
- Brackets optional but improve readability.

---

## 4. The `in` Keyword and Truthiness
- `in` checks membership:
  - `if "admin" in roles:` → checks if `"admin"` is in list
  - Works on strings: `if "@" in email:` → checks for valid email format
- **Truthiness**:
  - Empty strings, `0`, `None`, empty lists → falsy
  - Non-empty values → truthy
  - Example: `if username:` → valid check for non-empty string

---

# Unit 6 – Repeating Tasks

## 1. The for Loop
- Repeats a block of code for each item in a sequence.
- Examples:
  - `for student in students:` → iterates list
  - `for i in range(5):` → iterates 0–4
  - `for key, value in contact.items():` → iterates dictionary pairs
- **Indentation is mandatory**.

---

## 2. The range() Function
- Generates a sequence of numbers.
- Patterns:
  - `range(5)` → 0–4
  - `range(1, 11)` → 1–10
  - `range(0, 20, 2)` → even numbers 0–18
  - `range(10, 0, -1)` → countdown 10–1
- Memory-efficient → generates numbers on demand.

---

## 3. The while Loop
- Runs as long as condition is `True`.
- Used when number of iterations is unknown.
- Example: read input until user types `"quit"`.
- Must update condition variable inside loop.
- Forgetting this creates an **infinite loop**.
- Stop infinite loop with **Ctrl+C**.

---

## 4. break and continue
- `break` → exits loop immediately.
- `continue` → skips rest of current iteration, moves to next.
- Use cases:
  - `break` → stop when condition met.
  - `continue` → skip items failing condition.
- Work in both **for** and **while** loops.
