Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")
        myobjectx = MyClass()
        myobjectx.variable

        


class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")
myobjectx = MyClass()
SyntaxError: invalid syntax
myobjectx.variable
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myobjectx.variable
NameError: name 'myobjectx' is not defined. Did you mean: 'object'?
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")

        
myobjectx = MyClass()
myobjectx.variable
'blah'
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")

        
myobjectx = MyClass()
print(myobjectx.variable)
blah
class MyClass:
    variable = "blah"
    def function(self):
       rint("This is a message inside the class.")

       
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")

        
myobjectx = MyClass()
myobjecty = MyClass()
myobjecty.variable = "yackity"
print(myobjectx.variable)
blah
print(myobjecty.variable)
yackity
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")

        
myobjectx = MyClass()
myobjectx.function()
This is a message inside the class.
class NumberHolder:
    def __init__(self, number):
        self.number = number
    def returnNumber(self):
        return self.number
var = NumberHolder(7)
SyntaxError: invalid syntax
class NumberHolder:
    def __init__(self, number):
        self.number = number
    def returnNumber(self):
        return self.number
    var = NumberHolder(7)
    print(var.returnNumber())

    
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    class NumberHolder:
  File "<pyshell#65>", line 6, in NumberHolder
    var = NumberHolder(7)
NameError: name 'NumberHolder' is not defined
class NumberHolder:
    def __init__(self, number):
        self.number = number
    def returnNumber(self):
        return self.number

    
var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'
7
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
Fer is a red convertible worth $60000.00.
print(car2.description())
Jump is a blue van worth $10000.00.
