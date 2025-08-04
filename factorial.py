#This is the code to find factorial of any number
n = int(input("Enter a number :"))
i = 1
fac = 1
while n >= i :
    fac*=i
    i+=1
    
print ("Factorial of " + str(n) +" is " + str(fac))