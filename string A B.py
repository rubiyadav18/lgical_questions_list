n=int(input("enter a number"))
a=["a","b",]
i=1
empty1=[ ]
while i<=n:
    empty2=[ ]
    j=0
    while j<len(a):
        c=a[j]
        s=str(i)
        b=c+s
        empty1.append(b)
        empty2.append(empty1)
        j=j+1
    i=i+1
print(empty1)