class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        """Add a new contact to the contact book."""
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """Display all contacts in the contact book."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        """Search for a contact by name or phone number."""
        results = [
            (name, details) for name, details in self.contacts.items()
            if search_term.lower() in name.lower() or search_term in details['phone']
        ]
        if not results:
            print("No contact found.")
        else:
            print("\n--- Search Results ---")
            for name, details in results:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name):
        """Update the details of an existing contact."""
        if name not in self.contacts:
            print("Contact not found.")
        else:
            print("Enter new details (leave blank to keep existing):")
            phone = input(f"New Phone ({self.contacts[name]['phone']}): ") or self.contacts[name]['phone']
            email = input(f"New Email ({self.contacts[name]['email']}): ") or self.contacts[name]['email']
            address = input(f"New Address ({self.contacts[name]['address']}): ") or self.contacts[name]['address']
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print(f"Contact '{name}' updated successfully.")

    def delete_contact(self, name):
        """Delete a contact from the contact book."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")

    def main_menu(self):
        """Display the main menu and handle user interaction."""
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    name = input("Enter Name: ")
                    phone = input("Enter Phone Number: ")
                    email = input("Enter Email: ")
                    address = input("Enter Address: ")
                    self.add_contact(name, phone, email, address)
                elif choice == 2:
                    self.view_contacts()
                elif choice == 3:
                    search_term = input("Enter Name or Phone Number to search: ")
                    self.search_contact(search_term)
                elif choice == 4:
                    name = input("Enter the name of the contact to update: ")
                    self.update_contact(name)
                elif choice == 5:
                    name = input("Enter the name of the contact to delete: ")
                    self.delete_contact(name)
                elif choice == 6:
                    print("Exiting Contact Book. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Error: Please enter a valid number.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.main_menu()
