# 1. Write a python script to calculate sum of first N natural numbers




N=int(input("Enter the value of N: "))

i=1
s=0
while(i<=N):
    s=s+i 
    i+=1
print("Sum of first %d natural numbers is"%N,s)    