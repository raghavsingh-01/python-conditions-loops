#This the program in which it takes input of numbers to the list and then count even and odd numbers in it

list=[]
n = 0
e,o=0,0
print("NOTE : If all the numbers in list are entered then just press enter key then the result is shown !")

while  n != 1:
    
    num=input("Enter the number :")
    
    if num!="" :
        num=int(num)
        list.append(num)
        if (num%2==0) :
            e+=1
        else :
            o+=1
    else :
         print(list)
         print("In this list there are",e,"Even numbers", end=" ")
         print("and",o,"Odd numbers")
         n=1
               