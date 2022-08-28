# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)

num=int(input("Enter a number: "))

x=num
bin=0
i=0
while(x):
    rem=x%2
    bin+=rem*(10**i)
    x//=2
    i+=1

print("Binary number=%d"%bin)

