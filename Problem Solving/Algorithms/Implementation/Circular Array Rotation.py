def nth_perm(v, n):   
    l=len(v)
    a=[0]*l
    for i in range(0,l):
        a[(i+n)%l]=v[i]
    return a

a=[int(x) for x in input().split()]
n=a[0]
k=a[1]
q=a[2]
a=[int(x) for x in input().split()]
a=nth_perm(a,k)
for i in range(0,q):
    print(a[int(input())])