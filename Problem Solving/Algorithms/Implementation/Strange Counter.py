import sys

a1 = [1]
a2 = [3]

t = int(input())

br = int(1)
while (a1[-1] <= t):
	a1.append(a1[br-1] + a2[br-1])
	a2.append(a2[br-1] * 2)
	br += 1

res = a2[-2] - (t - a1[-2])

print(res)