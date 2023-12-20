import json

# File to store contacts data
CONTACTS_FILE = "contacts.json"

# Load existing contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

# Function to display the main menu
def display_menu():
    print("\n==== Contact Management System ====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    email = input("Enter the contact email: ")
    address = input("Enter the contact address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\n==== Contact List ====")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

# Function to search for a contact by name or phone number
def search_contact(contacts):
    query = input("Enter the contact name or phone number to search: ")
    search_results = []

    for contact in contacts:
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            search_results.append(contact)

    if not search_results:
        print("No matching contacts found.")
    else:
        print("\n==== Search Results ====")
        for result in search_results:
            print(f"{result['name']} - {result['phone']}")

# Function to update contact details
def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        contact_index = int(input("Enter the contact number to update: "))
        if 1 <= contact_index <= len(contacts):
            contact = contacts[contact_index - 1]
            print(f"\nUpdating details for {contact['name']}:")
            contact["name"] = input("Enter new name (press Enter to keep the same): ") or contact["name"]
            contact["phone"] = input("Enter new phone number (press Enter to keep the same): ") or contact["phone"]
            contact["email"] = input("Enter new email (press Enter to keep the same): ") or contact["email"]
            contact["address"] = input("Enter new address (press Enter to keep the same): ") or contact["address"]

            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        contact_index = int(input("Enter the contact number to delete: "))
        if 1 <= contact_index <= len(contacts):
            deleted_contact = contacts.pop(contact_index - 1)
            save_contacts(contacts)
            print(f"Contact {deleted_contact['name']} deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the Contact Management System
def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
