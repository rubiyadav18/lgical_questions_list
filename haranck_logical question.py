z=int(input())
for i in range(z):
	k1,k2,k3,c=[float(x) for x in input().split()]
	x=k1*k2*k3*c
	x=round((100/x), 2)

	if x<9.58:
		print("yes")
	else:
		print("no")