a = [10,20,30,20,10,50,60,40,80,2,2,3,3,31]
i=0
empty=[ ]
index=0
while i<len(a):
    if a[i] not in empty or index>0:
        empty.append(a[i])
    i=i+1
print(empty)

    