#creating a contact book simulator
#name the list

contacts = [{'name': 'Thuto Mpotsang', 'Phone': '0781234567', 'email': 'Thutompotsang@yahoo.com'},
            {'name': 'Thobani Nemtanjela', 'Phone': '0721234567', 'email': 'Tnemtanjela@yahoo.com'},
            {'name': 'Selvyn Williams', 'Phone': '0831234567', 'email': 'Williamsselvyn@yahoo.com'},
            {'name': 'Deandre Odumbuwale', 'Phone': '0641234567', 'email': 'Deodumbuwale@yahoo.com'}]


while True:
    print("Choose an option")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Exit")

    choice = input("Please select choice from menu above: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email adress: ")
        contacts.append({'name': name, 'phone': phone, 'email': email})
        print(f"{name} added successfully")
    
    elif choice == "2":
        search = input("Contact name: ")
        found = False

        for contact in contacts:
            if contacts['name'] == search:
                print(f"Contact found, {contact}")
                found = True
                break
        if not found:
            print("Contact not found. ")
    
    elif choice == "3":
        delete = input("Please enter name of contact you would like to Delete: ")
        found = False
        for contact in contacts:
            if contact['name'] == delete:
                contacts.remove(contact)
                print(f"{delete} deleted successfully")
                found = True
                break
        if not found:
            print("Contact not found.")
    
    elif choice == "4":
        print(f"All contacts ({len(contacts)})")
        print(contacts)
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("invalid response try again")
