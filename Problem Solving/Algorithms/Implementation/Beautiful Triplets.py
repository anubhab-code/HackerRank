def beau(nums, d):
    count = 0
    for num in nums:
        if (num + d) in nums and (num + 2*d) in nums:
            count += 1
    return count


n, d = tuple(int(i) for i in input().strip().split(" "))
nums = [int(i) for i in input().strip().split(" ")]
print(beau(nums, d))