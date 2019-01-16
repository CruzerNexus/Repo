import os

dataDir = '../..'
dataPath = os.path.join(dataDir, 'contactListTemp - Sheet1.csv')
print(dataPath)
with open(dataPath) as file:
    lines = file.read().split('\n')
    print(lines)

headers = lines[0].split(",")
print(headers)
contactList = []
for i in range(1, len(lines), ):
    if i == -1:
        break
    row = lines[i].split(",")
    print(headers)
    contactList.append(dict(zip(headers, row)))
print(contactList)
'''
def contactList(lines):
    contacts = []
    for i in range(len(headers)):
        contacts[headers[i]] = lines[i + 1]
'''
