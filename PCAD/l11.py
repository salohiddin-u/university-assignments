contacts = {}

number_of_contacts = int(input("Enter the number of contacts: "))
for i in range(number_of_contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter contact phone number: ")
    contacts[name] = phone_number

print("Do you want to search for a contact? (yes/no) ")

choice = input().lower()

while choice == "yes":
    search_name = input("Enter the name of the contact you want to search for: ")
    if search_name in contacts:
        print(f"Phone number of {search_name}: {contacts[search_name]}")
    else:
        print(f"{search_name} not found in contacts.")
    
    print("Do you want to search for another contact? (yes/no) ")
    choice = input().lower()

print("Your contacts:")
for name, phone_number in contacts.items():
    print(f"Contact Name: {name}, Phone Number: {phone_number}")