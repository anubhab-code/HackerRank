s = int(input())
ar = [int(x) for x in input().split()]
x = ar[s-1]

i = s - 2
while True:
    ar[i + 1] = ar[i]
    i = i - 1
    for n in ar: print(n, end=' ')
    print()
    if i == -1 or x >= ar[i]:
        break

ar[i + 1] = x

for x in ar: print(x, end=' ')