list=[1,2,3,4,5,6,7,8,9,10]
e=0
o=0
empty1_even=[ ]
empty2_odd=[ ]
i=0
while i<len(list):
    if list[i]%2==0:
        e=e+1
        empty1_even.append(list[i])
    else:
        o=o+1
        empty2_odd.append(list[i])
    i=i+1
output=[["even",e,empty1_even],["odd",o,empty2_odd]]
print(output)