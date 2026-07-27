#prompt user to enter passsword
password = input("Please enter your Password: ")

#strip the extra spaces at the end and at the beginning
password = password.strip()

#make a hint concatenation using indexing
hint = password[0] + password[-1]

#print the hint by indexing the hint variable
print(f"Your password hint: It starts with {hint[0]} and ends with {hint[-1]}")