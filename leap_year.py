#This is the program to find the entered year is a leap year or not
n = int(input("Enter the year :"))

# leap year condition
c = 0
if (n%100 == 0) :
    if (n%400 == 0) :
        c = 1
    else:
         c = 0
elif(n % 4 == 0):
    c = 1
else:
    c = 0
    
if (c == 1) :
    print("Leap Year")
else :
    print("Not a leap year")
