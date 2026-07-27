
contacts = {'Thuto': '0678856787', 'Thabiso': '0786789101', 'Shosha': '0764567891'}

search = input("please enter the name of the contact to search: ").title()

if search in contacts:
    print(f"Contact found, {search} : {contacts[search]}")
else:
    print("Contact not found")