contact_list = []

while True:
    contact_name = input("Enter contact name (or type 'done' to finish): ")
    if contact_name.lower() == 'done':
        if len(contact_list) > 0:
            with open("contacts.txt", "a") as contact_file:
                for item in contact_list:
                    contact_file.write(f"{item['name']}: {item['number']}\n")                
        quit()

    contact_number = input(f"Enter phone number for {contact_name}: ")

    contact_list.append({"name": contact_name, "number": contact_number})

