import sys

s = input().strip()

count=1
for i in s:
    count+=i.isupper()
    
print(count)