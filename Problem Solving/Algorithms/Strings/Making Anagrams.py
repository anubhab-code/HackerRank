str1 = input()
str2 = input()
a = [0 for i in range(0,27)]
for i in str1:
    a[ord(i)-ord('a')] += 1
for i in str2:
    a[ord(i)-ord('a')] -= 1

ans = 0
for i in a:
    if ( i < 0 ):
        ans += -i
    else:
        ans += i
print(ans)