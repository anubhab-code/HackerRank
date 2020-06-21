p = int(input())
q = int(input())

result=[]
for i in range(p,q+1,1):
    k = i**2
    r = k % (10 ** len(str(i)))
    l = k // (10 ** len(str(i)))
    if i == int(r)+int(l):
            result.append(i)
 
result= list(set(result))
result.sort()
if len(result) == 0:
    print ('INVALID RANGE')
else:
    print (' '.join([str(i) for i in result]))