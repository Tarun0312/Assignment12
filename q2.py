# 2. Write a python script to calculate sum of squares of first N natural numbers

N=int(input("Enter the number: "))

i=1
sq=0

while(i<=N):
    sq=sq+i*i
    i+=1
print("Sum of squares of first %d natuarl numbers is"%N,sq)    