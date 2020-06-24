num = input()
pivot, *ar = input().split()

left = [x for x in ar if int(x) <= int(pivot)]
right = [x for x in ar if int(x) > int(pivot)]

print(" ".join(left+[pivot]+right))