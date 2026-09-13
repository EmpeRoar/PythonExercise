phonebook = {}
phonebook["John"] = "555-1234"
phonebook["Jane"] = "555-5678"  
print(phonebook)

for name, number in phonebook.items():
    print(f"{name}: {number}")

if "John" in phonebook:
    print("John's number is:", phonebook["John"])  
if "Alice" not in phonebook:
    print("Alice is not in the phonebook.")    