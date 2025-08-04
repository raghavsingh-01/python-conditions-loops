#This the program to find the sum of digits of a number

sum = 0
n= int(input("Enter Number : "))
le = len(str(n))

for i in range(le) :
    d = n%10
    sum += d
    n =n//10
    
print("Sum : " +str(sum))    