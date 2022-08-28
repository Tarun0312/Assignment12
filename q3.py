# 3. Write a python script to calculate sum of cubes of first N natural numbers

N=int(input("Enter the number: "))

i=1
sc=0

while(i<=N):
    sc+=i*i*i
    i+=1
print("Sum of cubes of first %d natural numbers is %d"%(N,sc))   