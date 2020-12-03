list=[[2,3,4],[3,4,6],[6,7,8],]
i=0
while i<len(list):
    j=0
    empty=[ ]
    while j<len(list[i]):
        if list[i][j]==6:
            empty.append(list[i][j])
        j=j+1
    i=i+1
print(empty)
            