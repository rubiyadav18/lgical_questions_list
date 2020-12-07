num=int(input("enter a number"))
num1=num
rem=0
sum=0
while num1>0:
    rem=num1%10
    sum=sum+rem
    num1=num1//10
print(sum)
if num%sum==0:
    print("it is harsad number")
else:
    print("it is not harsad number")