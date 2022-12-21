Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
astring = "Hello world!"
astring2 = 'Hello world!'

astring = "Hello world!"
print("single quotes are ' '")
single quotes are ' '
print(len(astring))
12
astring = "Hello world!"
print(astring.index("o"))
4
astring = "Hello world!"
print(astring.count("l"))
3
astring = "Hello world!"
print(astring[3:7])
lo w
astring = "Hello world!"
print(astring[3:7:2])
l 
astring = "Hello world!"
print(astring[3:7])
lo w
print(astring[3:7:1])
lo w
astring = "Hello world!"
print(astring[::-1])
!dlrow olleH
astring = "Hello world!"
print(astring.upper())
HELLO WORLD!
print(astring.lower())
hello world!
astring = "Hello world!"
print(astring.startswith("Hello"))
True
print(astring.endswith("asdfasdfasdf"))
False
astring = "Hello world!"
afewwords = astring.split(" ")

afewwords = astring.split(" ")
