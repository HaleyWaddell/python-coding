Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 2
print(x == 2) # prints out True
True
print(x == 3) # prints out False
False
print(x < 3) # prints out True
True
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
    if name == "John" or name == "Rick":
        print("Your") name is either John or Rick.
        
SyntaxError: invalid syntax
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

    
Your name is either John or Rick.
statement = False
another_statement = True
if statement is True:
    pass
elif another_statement is True:
    pass
else:
    pass


x = 2
if x == 2:
    print("x equals two!")
    else:
        
SyntaxError: invalid syntax

x = 2
if x == 2:
    print("x equals two!")
    else:
        
SyntaxError: invalid syntax
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

    
x equals two!

x = [1,2,3]

y = [1,2,3]
print(x == y)
True
print(x is y)
False

print(not False)
True
print((not False) == (False))
False
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]
if number > 15:
    print("1")

    
1
if first_array:
    print("2")

    
2
if len(second_array) == 2:
    print("3")

    
3
if len(first_array) + len(second_array) == 5:
    print("4")

    
4
if first_array and first_array[0] == 1:
    print("5")

    
5
if not second_number:
    print("6")

    
6
