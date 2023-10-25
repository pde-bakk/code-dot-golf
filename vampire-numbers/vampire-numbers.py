S,R=sorted,range(10,1001)
print(*S(set(i*j for i in R for j in R if all([len(f:=S(str(i)+str(j)))%2<1,i%10 or j%10,S(str(i*j))==f]))),sep='\n')
