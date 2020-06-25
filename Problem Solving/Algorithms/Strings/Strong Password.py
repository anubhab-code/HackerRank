n = int(input())
s = input()
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
ans = 0
for req in [numbers, lower_case, upper_case, special_characters]:
    for c in req:
        if c in s:
            break
    else:
        n += 1
        ans += 1
while n < 6:
    n += 1
    ans += 1
print(ans)