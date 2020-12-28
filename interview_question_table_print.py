num=int(input("enter a number"))
i=0
empty1=[ ]
while i<=num:
    j=1
    empty2=[]
    empty3=[] 
    empty3.append(i)
    while j<=10:
        s=i*j
        empty2.append(s)
        j=j+1
    empty3.append(empty2)
    i=i+1
print(empty3)
