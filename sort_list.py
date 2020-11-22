a=[3, 6, 4, 2, 7, 8, 9, 11, 12, 0, 1]
index=0
while index<len(a):
    j=0
    while j<index:
        if a[index]>a[j]:
            b=a[index]
            a[index]=a[j]
            a[j]=b
        j=j+1
    index=index+1
print("a",a)
