# 8. Write a python script to calculate sum of digits of a given number

num=int(input("Enter a number: "))

x=num
s=0

while(x):
    s+=x%10
    x//=10

print("Sum of digits of given number %d=%d"%(num,s))    