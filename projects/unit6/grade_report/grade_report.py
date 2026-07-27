learners = [
    {'name': 'Thuto', 'math': 70, 'english': 80, 'Science': 95},
    {'name': 'Tsholo', 'math': 65, 'english': 84, 'Science': 70},
    {'name': 'Samkelo', 'math': 83, 'english': 80, 'Science': 91},
    {'name': 'Selaoloane', 'math': 70, 'english': 61, 'Science': 56},
    {'name': 'Tlharesakgosi', 'math': 90, 'english': 95, 'Science': 89}
]

results = []          # store each student’s report
averages = []         # store all averages for class stats

for student in learners:
    learner_avg = round((student['math'] + student['english'] + student['Science']) / 3, 2)
    averages.append(learner_avg)   # keep track of averages

    # Grade logic
    if learner_avg >= 80:
        grade = "A"
    elif learner_avg >= 70:
        grade = "B"
    elif learner_avg >= 60:
        grade = "C"
    elif learner_avg >= 50:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail
    if learner_avg >= 50:
        status = "Pass"  
    else:
        "Fail"

    results.append({
        'name': student['name'],
        'Average': learner_avg,
        'Grade': grade,
        'Status': status
    })

# Class statistics
class_average = round(sum(averages) / len(averages), 2)
highest_mark = max(averages)
lowest_mark = min(averages)

# Display report
print("=== CLASS REPORT ===")
for r in results:
    print(f"{r['name']}: Avg={r['Average']} Grade={r['Grade']} Status={r['Status']}")

print("\n--- CLASS STATS ---")
print(f"Class Average: {class_average}")
print(f"Highest Average: {highest_mark}")
print(f"Lowest Average: {lowest_mark}")

# Search loop
while True:
    search_name = input("\nEnter a student name to search (or 'exit' to quit): ")
    if search_name.lower() == "exit":
        break
    found = False
    for r in results:
        if r['name'].lower() == search_name.lower():
            print(f"Found: {r}")
            found = True
            break
    if not found:
        print("Student not found.")
