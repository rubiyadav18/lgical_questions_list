for i in range(int(input())):
	b=input().split()
	c=input()
	k='*'*int(b[1])
	if k in c:
		print('YES')
	else:
		print('NO')