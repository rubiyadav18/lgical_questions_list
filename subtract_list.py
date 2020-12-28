list=[3,4,5,]
list2=[6,7,2]
i=0
empty=[ ]
multi=1
while i<len(list):
    multi=list[i]-list2[i]
    empty.append(multi)
    i=i+1
print(empty)