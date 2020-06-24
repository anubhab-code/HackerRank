import sys

V = int(input())
n = int(input())
i = 0
for cur in input().split():
    if (V == int(cur)):
        print(i)
    i += 1