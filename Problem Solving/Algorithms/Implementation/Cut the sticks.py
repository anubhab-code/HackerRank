n = int(input())
sticks = list(map(int, input().split()))

uniq = sorted(set(sticks))

for i in uniq:
	print(len([x for x in sticks if x >= i]))