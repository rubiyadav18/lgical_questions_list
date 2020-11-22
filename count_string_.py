list=['abc', 'xyz', 'aba', '1221']
count=0
index=0
while index<len(list):
    if len(list[index])> 1and list[index][0]==list[index][-1]:
        count=count+1
    index=index+1
print(count)


 