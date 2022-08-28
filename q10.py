# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)

num=int(input("Enter the  number: "))

i=0
oct=0
while(num):
    rem=num%8
    oct+=rem*(10**i)
    num//=8
    i+=1


   

print("Octal equivalent=",oct)    

