Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
myint = 7
print(myint)
7
myfloat = 7.0
print(myfloat)
7.0
myfloat = float(7)
print(myfloat)
7.0
mystring = 'hello'
print(mystring)
hello
mystring = "hello"
print(mystring)
hello
mystring = "Don't worry about apostrophes"
print(mystring)
Don't worry about apostrophes
one = 1
two = 2
three = one + two
print(three)
3
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
hello world
a, b = 3, 4
print (a, b)
3 4
one = 1
two = 2
hello = "hello"
print(one + two + hello)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(one + two + hello)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
one = 1
two = 2
hello = "hello"

print(one + two + hello)
SyntaxError: multiple statements found while compiling a single statement
one = 1
two = 2
hello = "hello"

print(one + two + hello)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(one + two + hello)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
