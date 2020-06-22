t = int(input())
while t > 0:
    t -= 1
    n,m,s = map(int, input().strip().split(' '))
    k = (s+m-1)%n
    if(k==0):
        print (n)
    else:
         print (k)   