i=1
while 10001>i:
 if sum(D:=[d for d in range(1,i+1)if i%d<1])/len(D)%1==0:print(i)
 i+=1
