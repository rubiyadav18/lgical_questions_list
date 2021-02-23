col=int(input("enter a any collom---"))
rows=int(input("enter a any rows---"))
empty=[]
i=1
k=1
empty3=[]
while i<=rows:
    j=1
    empty2=[]

    while j<=col:

        empty2.append(k)
        empty3.append(empty2)
        k+=1
        j=j+1
    empty.append(empty2)
    empty3.append(empty)

    i=i+1
n=0
while n<len(empty):

	print(empty[n])
	print()
	n+=1
















# a=[1,2,3,4,5,6,7,8,9]
# num=int(input("enter a any number--"))
# # i=-1
# # while i>=-num:
# #     print(a[i])
# #     i=i-1
# k=1
# while k>=num:
#     print(a[k])
#     k=k+1
# i=1
# while i<len(a):
#     j=1
#     while j<len(a):
#         print(a[i],a[j])
#         j=j+1
#     i=i+1
