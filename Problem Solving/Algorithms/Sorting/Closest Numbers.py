n=int(input())
ar=input().split()
ar=[int(ar[i]) for i in range(n)]
ar.sort()
dif=[]
for i in range(1,n):
    dif.append((ar[i]-ar[i-1]))
sdif=ndif=min(dif)
while sdif==ndif:
    print(ar[dif.index(sdif)],ar[dif.index(sdif)+1],end=" ")
    dif[dif.index(sdif)]+=1
    ndif=min(dif)