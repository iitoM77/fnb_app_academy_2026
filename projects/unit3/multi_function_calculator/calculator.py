# Set variable names
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# make calculations & print
print(f"Addition '+': {str(round(first_number + second_number, 2))}")
print(f"Subtraction '-': {str(round(first_number - second_number, 2))}")
print(f"Multiplication '*': {str(round(first_number * second_number,2))}")

#Helps handle input of zero on either input
if second_number == 0 or first_number == 0:
    print(f"Sorry you can't perform the faction containing 0")
    print(f"Sorry you can't perform the faction containing 0")
else:
    print(f"Division '//': {str(round(first_number // second_number, 2))}")
    print(f"modulus '%': {str(first_number % second_number)}")