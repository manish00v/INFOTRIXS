import csv 
filename  = "contact.csv"

class Contacts:
    
    def _init_(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        
        
class ContactManager:
    def _init_(self, filename):
        self.contacts = []
        self.filename = filename   
        
    def load_contacts_from_file(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    name, phone, email = row
                    contact = Contacts(name, phone, email)
                    self.contacts.append(contact)
        except FileNotFoundError:
            print("Contact file not found. Starting with an empty contact list.") 
            
            
    def save_contacts_to_file(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email'])
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email])
        print(f"Contacts saved to {self.filename}.")
        
    def add_contact(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
        
        
        contact = Contacts(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully.")
        self.save_contacts_to_file() 
        
    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print("Search results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("No contacts found.") 
            
    def update_contact(self, name, new_phone, new_email):
        updated = False
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                contact.phone = new_phone
                contact.email = new_email
                updated = True
        if updated:
            print("Contact updated successfully.")
            self.save_contacts_to_file()
            
        else:
            print("Contact not found.")


def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        
        contact_manager = ContactManager("contacts.csv")
        contact_manager.load_contacts_from_file()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            
            name = input("entar name :")
            phone = input("enter phone:")
            email = input("enter email :")
            
            contact_manager.add_contact(name,phone,email)
            
            
        elif choice == '2':
            
            name = input("entar name :")
            contact_manager.search_contact(name)
            
        elif choice == '3':
            name = input("entar name :")
            phone = input("enter phone:")
            email = input("enter email :")
            contact_manager.update_contact(name , phone , email)
            
            
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '_main_':
    main()