import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = 0
    x = 1  
    y = 2  
    while x <= n:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    print(ans)