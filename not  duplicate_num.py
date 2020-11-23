a = [10,20,30,20,10,50,60,40,80,50,40,5,5,6,6]
i=0
empty=[ ]
while i<len(a):
    j=i+1
    index=0
    while j<len(a):
        if a[i]==a[j]:
            index=index+1
        j=j+1
    if a[i] not in empty or index>0:
        empty.append(a[i])
    i=i+1
print(empty)
            
    