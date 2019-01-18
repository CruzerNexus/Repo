# contactListV2.py


headers = ["C.O.", "Ship", "Squadron"]
contacts = []


def createRecord(att1, att2, att3):
    newContact = [att1, att2, att3]
    contacts.append(dict(zip(headers, newContact)))
    return contacts[-1]


def retrieveRecord(search):
    for i, contact in enumerate(contacts):
        if contact["C.O."] == search:
            print("Contact found: ")
            return contacts[i]
    print("Contact not found.")
    return -1

def updateRecord(update):
    print(retrieveRecord(update))
    toChange = retrieveRecord(update)
    for i in toChange
    change = input("What information would you like to update? ")
    if change == 


print('**Welcome to the AAP Officer database!**')
while True:
    action = input("What action do you wish to perform(create/retrieve/update/delete)? ").lower()
    if action == "create":
        att1 = input("Enter the commanding officer: ").lower()
        att2 = input("Enter their ship: ")
        att3 = input("Enter their perfered squadron: ")
        print(createRecord(att1, att2, att3))
        complete = input("Finished adding contacts?(y/n): ").lower()
        if complete == "y":
            print("Entry complete. Signing off...")
            break
    elif action == "retrieve":
        search = input("Enter the name of the commanding officer you wish to view: ").lower()
        print(retrieveRecord(search))
    elif action == "update":


