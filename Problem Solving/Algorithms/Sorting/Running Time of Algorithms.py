s = int(input())
input_ar = input().split()
ar = [int(x) for x in input_ar]

shift_count = 0
for i in range(1, s):
    j = i - 1
    if ar[i] >= ar[j]:
        continue
    v = ar[i]
    while v < ar[j] and j >= 0:
        ar[j + 1] = ar[j]
        shift_count += 1
        j -= 1
    ar[j + 1] = v

print(shift_count)