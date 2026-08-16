class ContactManager:
    def __init__(self):
        self.contacts = []

    # 1.Add contact
    def add_contact(self,name,mobile,email):
        contact = {"name": name, "mobile": mobile, "email": email}
        self.contacts.append(contact)
        print("Contact added successfully!")

    # 2.Update contact
    def update_contact(self, old_mobile, new_mobile):
        for i in self.contacts:
            if i["mobile"] == old_mobile:
                i["mobile"] = new_mobile
                print("Mobile number updated successfully!")

    # 3. List of contacts
    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")
            for i in self.contacts:
                print(f"Name: {i['name']} | Mobile: {i['mobile']} | Mail: {i['email']}")

    # 4. Delete contact
    def delete_contact(self, name):
        for i in self.contacts:
            if i["name"] == name:
                self.contacts.remove(i)
                print(f"Name {name} Deleted")

system = ContactManager()

while True:
    print("\n1. Add contact")
    print("2. Update contact")
    print("3. List of contacts")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        mobile = input("Enter Mobile: ")
        email = input("Enter Mail: ")
        system.add_contact(name, mobile, email)

    elif choice == "2":
        old_mob = input("Enter old mobile: ")
        new_mob = input("Enter new mobile: ")
        system.update_contact(old_mob, new_mob)

    elif choice == "3":
        system.display_contacts()

    elif choice == "4":
        number = input("Enter name to delete: ")
        system.delete_contact(name)

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid")