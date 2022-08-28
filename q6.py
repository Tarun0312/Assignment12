# 6. Write a python script to calculate factorial of a given number

N=int(input("Enter a number to calculate its factorial: "))

i=N
f=1

while(i>=1):
    f*=i
    i-=1
print("Factorial of %d is %d"%(N,f))    