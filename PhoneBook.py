# Phone Book Console App
# Written by: Derrick Minor
# Description: Simple shell contact phone book to allow users to enter and view contacts and phone numbers. Created for class to show different python commands
# Date: Jan 19, 2017

print("Welcome to Contact Phone Book")
n = 30
print ('*' * n)
contact = { }
contactList = input("\nTo add new contact, enter 'new' \n")
run = "true"
while (run == "true"):
        if (contactList == "view"):
            for key in contact:
                print("Contact Phone Book List: ")
                print("   " ,key, ":", contact[key], "\n")
        if (contactList == "new"):
            name = input("What is contact's name? ")
            phoneNum = input("What is contact's number? (XXX-XXX-XXXX) ")
            contact[name] = phoneNum
        else:
            print("Incorrect entry, please enter 'view' or 'new' ")
        run = "false"
        contactList = input("To view contact list, enter 'view' \nTo add new contact, enter 'new' \n")
        if (contactList == "view" or "new"):
            run = "true"
