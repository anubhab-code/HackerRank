
import sys


n = int(input().strip())
B = input().strip()

if (n < 3):
    print(0)
else:
    total = 0
    i = 2
    while (i < n):
        if (B[i-2:i+1] == '010'):
            total += 1
            i += 3
        else:
            i += 1
    print(total)