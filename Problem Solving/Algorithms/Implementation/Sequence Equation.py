n = int(input())
perm = [int(a)-1 for a in input().split()]
inv = [0]*n
for i,p in enumerate(perm):
    inv[p] = i
for i in range(n):
    print(inv[inv[i]]+1)