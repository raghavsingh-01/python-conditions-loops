#This is the code of simple calculator

print("Enter the number accordingly for arthimatic operations :")
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
i = int(input())

num1 = int(input("num 1 :"))
num2 = int(input("num 2 :"))

if(i == 1) :
    re = num1 + num2
elif(i == 2) :
    re = num1 - num2
elif(i == 3) :
    re = num1 * num2
elif(i == 4) :
    re = num1 // num2
    
print("Result:" + str(re))