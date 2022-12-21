Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
number = 1 + 2 * 3 / 4.0
print(number)
2.5
remainder = 11 % 3
print(remainder)
2
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
49
print(cubed)
8
helloworld = "hello" + " " + "world"
print(helloworld)
hello world
lostofhellos = "hello" * 10
print(lotsofhellos)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(lotsofhellos)
NameError: name 'lotsofhellos' is not defined. Did you mean: 'lostofhellos'?
print(lostofhellos)
hellohellohellohellohellohellohellohellohellohello
even_number = [2,4,6,8]
odd_number = [1,3,5,7]
all_numbers = even_number + odd_number
print(all_numbers)
[2, 4, 6, 8, 1, 3, 5, 7]
print([1,2,3] * 3)
[1, 2, 3, 1, 2, 3, 1, 2, 3]
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
bug_lists = x_list + y_list

print ("x_list contains %d objects" % len(x_list))
x_list contains 10 objects
print("y_list contains %d objects" % len(y_list))
y_list contains 10 objects
print("big_list conatins %d objects" % len(bug_list))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print("big_list conatins %d objects" % len(bug_list))
NameError: name 'bug_list' is not defined. Did you mean: 'bug_lists'?
print("big_list conatins %d objects" % len(bug_lists))
big_list conatins 20 objects

if x_list.count(x) == 10 and y_list.count(y) ==10;
SyntaxError: invalid syntax
if x_list.count(x) == 10 and y_list.count(y) ==10:
    print("Almost there...")
if bug_lists.count(x) == 10 and bug_lists.count(7) == 10:
    
SyntaxError: invalid syntax
