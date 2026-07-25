#collect: first name, surname, age, and a favourite number
first_name = input("Enter your First name: ")
surname = input("Enter your Surname: ")
age = int(input("Enter your age: "))
fav_numb = float(input("What's your favourite number: "))
full_name = (f"{first_name} {surname}")

#Display the greeting
print(f"Welcome: {full_name}!")

#Display the name in uppercase and title casing
print(f"Name in uppercase: {full_name.upper()}")
print(f"Name in Title case: {full_name.title()}")

#calculating and displaying the age in months
age = age * 12
print(f"Age in months: {str(age)}")

#rounding the favourite number to 2 decimals
print(f"your favourite number is: {round(fav_numb,2)}")

#printing the data type of each collected value
print("\nData types: ")
print(f"first_name: {type(first_name)}")
print(f"surname: {type(surname)}")
print(f"age: {type(age)}")
print(f"Favourite number: {type(fav_numb)}") 