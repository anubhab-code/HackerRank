s = int(input())
input_ar = input().split()
ar = [int(x) for x in input_ar]

for i in range(1, s):
    j = i - 1
    if ar[i] >= ar[j]:
        print(' '.join([str(x) for x in ar]))
        continue
    v = ar[i]
    while v < ar[j] and j >= 0:
        ar[j + 1] = ar[j]
        j -= 1
    ar[j + 1] = v
    print(' '.join([str(x) for x in ar]))