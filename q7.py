# 7. Write a python script to count digits in a given number

num=int(input("Enter a number to count it's digit: "))

count=0
x=num
while(x):
    x//=10
    count+=1
print("Total Digits in a number %d=%d"%(num,count))    
