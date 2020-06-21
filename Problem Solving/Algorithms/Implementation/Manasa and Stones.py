T= int(input())
for i in range(T):
    n=int(input())
    a=int(input())
    b=int(input())
    result=[]
    for j in range(n):
        result.append(j*a+(n-1-j)*b)
    result=list(set(result))
    result=sorted(result)
    print(" ".join(str(x) for x in result))