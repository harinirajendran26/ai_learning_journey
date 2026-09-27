class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def show_info(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

    # Step 2: storing contact in a list+ a function to add new ones
contacts = []
def add_contacts(contact_list, name, phone ,email):
    new_contact = Contact(name, phone, email)
    contact_list.append(new_contact)


add_contacts(contacts, "John Doe", "123-456-7890", "john.doe@example.com")
add_contacts(contacts, "Jane Smith", "987-654-3210", "jane.smith@example.com")

for contact in contacts:
    contact.show_info()

while True:
    print("\n-- Contact book Menu --")
    print("1. Add a new contact")
    print("2. Show all contacts")
    print("3.Search for a contact")
    print("4. Delete a contact")
    print("5. Save Contacts")
    print("6. Load Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contacts(contacts,name, phone, email)
        print("Contact added!")

    elif choice == "2":
        print("\n -- ALL Contacts --")
        for contact in contacts:
            contact.show_info()

    elif choice == "3":
        search_name = input("Enter the name to Search: ")
        found = False
        for contact in contacts:
            if contact.name == search_name:
                contact.show_info()
                found = True
        if not found:
                print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter the name to delete: ")
        for contact in contacts:
            if contact.name == delete_name:
                contacts.remove(contact)
                print("Contact deleted.")
                break

    elif choice == "5":
        with open("contacts.txt", "w") as file:
            for contact in contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")

    elif choice == "6":
        try:
            with open("contacts.txt", "r") as file:
                loaded_contacts = file.readlines()
                for line in loaded_contacts:
                    name, phone, email = line.split(",")
                    add_contacts(contacts, name.strip(), phone.strip(), email.strip())
                print("Contacts loaded successfully.")
        except FileNotFoundError:
            print("No saved contacts found yet. Save some first!")

    elif choice== "7":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")  
         
