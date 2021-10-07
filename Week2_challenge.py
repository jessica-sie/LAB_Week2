num = int(input("enter a number "))
if num % 11 == 0:
    print ("a",end='')
if num % 9 == 0:
    print ("b",end='')
if num % 7 == 0:
    print("c",end='')
if num % 2 == 0:
    print("d",end='')
if not(num % 11 == 0 or num % 7 == 0 or num % 9 == 0 or num % 2 == 0):
    print("ellosss")