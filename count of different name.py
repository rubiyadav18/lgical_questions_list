list=["rubi", "rubi", "megha", "sana", "sana","raam","syam",]
i=0
empty=[ ]
while i<len(list):
    j=0
    empty2=[ ]
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    if list[i] not in empty:
        empty.append(list[i])
        empty.append(count)
    if empty not in empty2:
        empty2.append(empty)
    
    i=i+1

print(empty)