L=[0,1]
while len(L)<31:L+=sum(L[-2:]),
print(*L,sep='\n')
