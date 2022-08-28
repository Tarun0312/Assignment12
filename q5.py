# 5. Write a python script to calculate sum of first N even natural numbers

N=int(input("Enter the number: "))

i=1
se=0

while(i<=N):
    se+=2*i
    i+=1
print("Sum of first %d odd natural numbers is %d"%(N,se))    