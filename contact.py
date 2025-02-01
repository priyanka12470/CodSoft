class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []  # A list to store contacts

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts saved.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"\nContact {i}:")
                print(contact)

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(contact)
                found = True
        if not found:
            print("No contact found.")

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name if name else contact.name
            contact.phone = phone if phone else contact.phone
            contact.email = email if email else contact.email
            contact.address = address if address else contact.address
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")

def display_menu():
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == "4":
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_manager.update_contact(index, name, phone, email, address)
        elif choice == "5":
            index = int(input("Enter the contact number to delete: ")) - 1
            contact_manager.delete_contact(index)
        elif choice == "6":
            print("Bye!!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
