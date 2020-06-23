import sys

def maxfactor(n, x=-1):
    while not n % 2:
        n //= 2
        x = 2
    for i in range(3, int(n ** .5) + 1, 2):
        while not n % i:
            n //= i
            x = i
    return n if n > 2 else x


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(maxfactor(n))