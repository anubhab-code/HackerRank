n, t = (int(i) for i in input().split())
wid = [int(i) for i in input().split()]

for i in range(t):
    a,b = (int(i) for i in input().split())
    print(min(wid[a:b+1]))