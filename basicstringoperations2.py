Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
s = "Strings are awesome!"
print("Length of s = %d" % len(s))
Length of s = 20
print("The first occurrence of the letter a = %d" % s.index("a"))
The first occurrence of the letter a = 8
print("a occurs %d times" % s.count("a"))
a occurs 2 times
print("The first five characters are '%s'" % s[:5])
The first five characters are 'Strin'
print("The next five characters are '%s'" % s[5:10])
The next five characters are 'gs ar'
print("The thirteenth character is '%s'" % s[12])
The thirteenth character is 'a'
print("The characters with odd index are '%s'" %s[1::2])
The characters with odd index are 'tig r wsm!'
print("The last five characters are '%s'" % s[-5:])
The last five characters are 'some!'
print("String in uppercase: %s" % s.upper())
String in uppercase: STRINGS ARE AWESOME!
print("String in lowercase: %s" % s.lower())
String in lowercase: strings are awesome!
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
    if s.endswith("ome!"):
        print("String ends with 'ome!'. Good!")
        print("Split the words of the string: %s" % s.split(" "))

        
String starts with 'Str'. Good!
String ends with 'ome!'. Good!
Split the words of the string: ['Strings', 'are', 'awesome!']
