#creating a grade classifier
#get the learner name, major & grades
learners = {'name': '' , 'major': ''}
learners['name'] = input("please enter learner name: ")
learners['major'] = input("please enter learner major: ")
math = float(input("Math: "))
physics = float(input("Physical Sciences: "))
bio = float(input("Biology: "))

#put all the values in a list of dictionaries to allow looping later
report = [{'Mathematics': math}, {'Physics': physics}, {'Biology': bio}]

#calculate the average
avg = (math + physics + bio)/3

#Assign the grade letter
if avg >= 80:
    letter_grade = "A"
elif avg >= 70 and avg <= 79:
    letter_grade = "B"
elif avg >= 60 and avg <= 69:
    letter_grade = "c"
elif avg >= 50 and avg <= 59:
    letter_grade = "D"
else:
    letter_grade = "F"

#assign pass status
if avg >= 50:
    pass_status = "Pass"
else:
    pass_status = "Fail"
 
#printing the report card
print(" ")
print(f"Report card for {learners['name']} doing {learners['major']}")
print(f"Math: {str(math)}%")
print(f"Physical Sciences: {str(physics)}%")
print(f"Biology: {str(bio)}%")
print(f"Course Average: {str(avg)}%")
print(f"Course Grade: {letter_grade}")
print(f"Course Outcome: {pass_status}")

#this loops through the report list to check for subjects that need intervention
for grade in report:
   for subject, mark in grade.items():
       if mark < 40:
           print(f"{learners['name']} needs intervention in {subject}")