Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
{'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
print(phonebook)
{'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

    
Phone number of John is 938477566
Phone number of Jack is 938377264
Phone number of Jill is 947662781
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
del phonebook["John"]
print(phonebook)
{'Jack': 938377264, 'Jill': 947662781}
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
phonebook.pop("John")
938477566
print(phonebook)
{'Jack': 938377264, 'Jill': 947662781}
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    
SyntaxError: invalid syntax
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
if "Jake" in phonebook:
    
SyntaxError: multiple statements found while compiling a single statement
honebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
if "Jake" in honebook:
    print("Jake is listed in the phonebook.")
    if "Jill" not in honebook:
        print("Jill is not listed in the phonebook.")

        
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
    if "Jill" not in phonebook:
        print("Jill is not listed in the phonebook.")

        
Jake is listed in the phonebook.
Jill is not listed in the phonebook.
