n = int(input())
arr = [int(i) for i in input().split()]

uniques = list(set(arr))
maxC = 0
maxNum = arr[0]

for num in uniques:
    if arr.count(num) > maxC:
        maxC = arr.count(num)
        maxNum = num
        
print(n - arr.count(maxNum))