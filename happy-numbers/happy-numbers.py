L=lambda x:sum(int(y)**2 for y in str(x))
for i in range(1,201):
	A=[L(i)]
	while A[-1]!=1 and A.count(A[-1])<2:A+=L(A[-1]),
	if 1 in A:print(i)
