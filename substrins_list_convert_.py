str="i am rubi yadav"
str=str.split(" ")
i=0
empty=[ ]
while i<len(str):
    if str[i]not in empty:
        empty.append(str[i])
    i=i+1
print(empty