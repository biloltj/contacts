address_book={}

def add_contact(address_book,name,phone,email,address):
    if name in address_book:
        print(f"Contact '{name}' already exists.")
    else:
        address_book[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} added successfully.")

def update_contact(address_book, name, phone=None, email=None, address=None):
    if name in address_book:
        if phone:
            address_book[name]["phone"] = phone
        if email:
            address_book[name]["email"] = email
        if address:
            address_book[name]["address"] = address
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def search_contact(address_book, name):
    contact = address_book.get(name)
    if contact:
        return f"{name}: Phone={contact['phone']}, Email={contact['email']}, Address={contact['address']}"
    else:
        return f"Contact '{name}' not found."
    
def display_contacts(address_book):
    if address_book:
        for name, details in address_book.items():
            print(f"{name}: Phone={details['phone']}, Email={details['email']},Address={details['address']}")
    else:
        print("Address book is empty.")

while True:
    print("Address book Menu:")
    print("1.Add contact:")
    print("2.Update contact:")
    print("3.Search contact:")
    print("4.Display contact:")
    print("5.Exit:")
    choice=input("Enter your choice:")
    if choice == "1":
        name=input("Enter the name:")
        phone=input("Enter phone:")
        email=input("email:")
        address=input("address:")
        add_contact(address_book,name,phone,email,address)
    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter new phone (or press Enter to skip): ")
        email = input("Enter new email (or press Enter to skip): ")
        address = input("Enter new address (or press Enter to skip): ")
        update_contact(address_book, name, phone or None, email or None, address or None)
    elif choice == "3":
        name = input("Enter name to search: ")
        print(search_contact(address_book, name))
    elif choice == "4":
        display_contacts(address_book)
    elif choice == "5":
        print("Exiting Address Book.")
        break
    else:
        print("Invalid choice")


