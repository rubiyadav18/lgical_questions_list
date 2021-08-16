num=int(input("enter  a number----"))
if num<1918:
    if num%4==0:
        print("12.09."+str(num))
    else:
        print("13.09."+str(num))
elif num>1918:
    if num%400==0 or (num%4==0 and num%100!=0):
        print("12.09."+str(num))
    else:
        print("13.09."+str(num))
else:
    print("13.09.1918")

    