# 4. Write a python script to calculate sum of first N odd natural numbers

N=int(input("Enter the number: "))

i=1
so=0

while(i<=N):
    so=so+2*i-1
    i+=1
print("Sum of first %d odd natural numbers is %d"%N%so)    
