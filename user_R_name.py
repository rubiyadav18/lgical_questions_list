list=["rubi","raam","raani","rabiya","dhannu","shubngi","message","nitin"]
i=0
empty=[]
user=input("enter a name")
while i<len(list):
    if list[i][0]==user:
        empty.append(list[i])
    i=i+1
print(empty)