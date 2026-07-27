#first I will prompt the user to insert their names and tell us a bit about themselve
first_name = input("Please enter your First name: ")
last_name = input("Please Enter your Surname: ")
full_name = f"{first_name} {last_name}"
bio = input("Please enter your Bio(tell us a bit about yourself: ")

#username creation
user_name = f"{first_name[0].lower()}{last_name}"

#replacing statements and getting the length of the bio
bio = bio.replace("I am","I'm")
bio_length = len(bio)

#printing the full data that was collected
print(f"Full_name: {full_name.title()}")
print(f"Username: {user_name.lower()}")
print(f"Bio: {bio.strip()}")
print(f"Number of characters in your Bio: {bio_length}")
