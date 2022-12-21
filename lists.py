Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
1
print(mylist[1]) # prints 2
2
print(mylist[2]) # prints 3
3
for x in mylist:
    print(x)

    
1
2
3
mylist = [1,2,3]
print(mylist[10])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(mylist[10])
IndexError: list index out of range
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]
print(numbers)
[1, 2, 3]
print(strings)
['hello', 'world']
print("The second name on the names list is %s" % second_name)
The second name on the names list is Eric
