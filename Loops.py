Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

    
2
3
5
7
for x in range(5):
   print(x)

   
0
1
2
3
4
for x in range(3, 6):
    print(x)

    
3
4
5
for x in range(3, 8, 2):
    print(x)

    
3
5
7
count = 0
while count < 5:
    print(count)
    count += 1

    
0
1
2
3
4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5
    
SyntaxError: expected ':'
    if count >= 5:
        
SyntaxError: unexpected indent
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        
SyntaxError: multiple statements found while compiling a single statement
count = 0
while True:
        print(count)
        count += 1
        if count >+ 5:
            break
        for x in range (10):
            if x % 2 = 0:
                
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
[DEBUG ON]
[DEBUG OFF]
count = 0
while True:
        print(count)
        count += 1
        if count >+ 5:
            break
        for x in range (10):
            if x % 2 = 0:
[DEBUG ON]
[DEBUG OFF]
count = 0
while True:
      print(count)count +=
      
SyntaxError: invalid syntax
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    for x in range(10):
        if x % 2 == 0:
            continue
        print(x)

        
0
1
3
5
7
9
1
1
3
5
7
9
2
1
3
5
7
9
3
1
3
5
7
9
4
count=0
while(count<5):
    print(count)
    count +=1
    else:
        
SyntaxError: invalid syntax
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
    for i in range(1, 10):
        if(i%5==0):
            break
        print(i)
else:
    
SyntaxError: invalid syntax
    else:
        
SyntaxError: unexpected indent
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
    for i in range(1, 10):
        if(i%5==0):
            break
        print(i)
    else:
        print("this is not printed because for loop is terminated because of break but not due to fail in condition")

        
0
1
2
3
4
count value reached 5
1
2
3
4
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399,162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67,104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,743, 527]
for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)

    
402
984
360
408
980
544
390
984
592
236
942
386
462
418
344
236
566
978
328
162
758
918
