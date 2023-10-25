def F(n,m=0):
	l=[]
	while n>0:r,n=n%10,n//10;l.append(r)
	while m>0:r,m=m%10,m//10;l.append(r)
	return sorted(l)
def cf(f1,f2):
	if f1*10<=f2 or f2*10<=f1:return 0
	v,f=F(f1*f2),F(f1,f2)
	return len(f)%2==0 and((f1%10)or(f2%10))and v==f
l=set()
for i in range(10,1001):
	for j in range(i,1001):
		if cf(i,j):l.add(i*j)
print(*sorted(l),sep='\n')
