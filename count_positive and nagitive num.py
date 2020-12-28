list=[ 35, - 40, - 201, 0, 66, - 78, 33, 0, - 13, 18]
index=0
count1=0
count2=0
count3=0
while index<len(list):
    if list[index]>0:
        count1=count1+1
    elif list[index]==0:
        count2=count2+1
    else:
        count3=count3+1
    index=index+1
print("count1 of positive number","-",count1)
print("count of negative number","-",count3)
print("count2 of zero number","-",count2)