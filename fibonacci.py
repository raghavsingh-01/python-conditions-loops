# Program to print Fibonacci series up to a maximum value

n = int(input("Enter the maximum value for the Fibonacci series: "))

sum = 0
n1 = 1
n2 = 0

print("Fibonacci series up to", n, ":")
while sum <= n:
    print(sum, end=" ")
    temp = n1
    n1 = sum
    n2 = temp
    sum = n1+n2