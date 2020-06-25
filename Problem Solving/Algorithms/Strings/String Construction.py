import sys

n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    p = ""
    cost = 0
    for letter in s:
        if letter not in p:
            cost += 1
        p += letter
    print(cost)