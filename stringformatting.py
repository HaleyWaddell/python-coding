Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
name = "John"
print("Hello, %s!" % name)
Hello, John!
name = "John"
age = 23
print("%s is %d years old." % (name, age))
John is 23 years old.
mylist = [1,2,3]
print("A list: %s" % mylist)
A list: [1, 2, 3]
data = ("John", "Doe", 53.44)
format_string = "Hello"
print(format_string % data)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(format_string % data)
TypeError: not all arguments converted during string formatting
data = ("John", "Doe", 53.44)
format_string = "Hello"
print(format_string % data)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(format_string % data)
TypeError: not all arguments converted during string formatting
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
Hello John Doe. Your current balance is $53.44.
