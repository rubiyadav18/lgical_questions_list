list=["rabiya","sana","rabiya","poonam","poonam","vandna"]
i=0
empty=[ ]
# i took empty list because i want to add remov duplicate string 
index=0
while i<len(list):
            if list[i] not in empty or index>0:
                empty.append(list[i])
            i=i+1
print(empty)
