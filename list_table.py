num1=int(input("enter a number"))
num2=int(input("enter a number="))
i=num1
empty=[ ]
while i<=num2:
    j=1
    empty2=[ ]
    empty3=[ ]
    empty3.append(i)
    while j<=10:
        z=i*j
        empty2.append(z)
        j=j+1
    empty3.append(empty)
    empty.append(empty2)
    i=i+1
print(empty)