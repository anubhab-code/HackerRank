import sys

def compute(N):
    s = sum(i for i in range(1, N + 1))
    s2 = sum(i*i for i in range(1, N + 1))
    return str(s**2 - s2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(compute(n))