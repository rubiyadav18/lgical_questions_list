i=1
n=5
while i<=4:
    j=n
    if i%2==0:
        while j>=n-4:
            print(j,end=" ")
            j=j-1
    else:
        while j-4<=n:
            print(j-4,end=" ")
            j=j+1        
    print()
    i=i+1
    n=n+5

