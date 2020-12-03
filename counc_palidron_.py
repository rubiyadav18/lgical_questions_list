list=['abc', 'xyz',"mama","66666", "papa","444",'aba',"nitin", '1221']
count=0
index=0
while index<len(list):
    if  list[index][0]==list[index][-1]:
        count=count+1
    index=index+1
print(count)