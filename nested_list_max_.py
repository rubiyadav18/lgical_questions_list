list=[[1,2,8],[4,5,10],[7,8,100],[10,11,12],[13,13,200],[9,35,55],]
empty=[ ]
# i took empty list because i want to add the numbers
index=0
while index<len(list):
    # i am using nested loop because i want to find max number from list thst why i am nested loop
    j=0
    max=0
    while j<len(list[index]):
        if max<list[index][j]:
            max=list[index][j]
        j=j+1
    empty.append(max)
    index=index+1
print(empty)
