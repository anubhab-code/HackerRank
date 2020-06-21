import sys

s = input().strip()
n = int(input().strip())

x=0 
for i in s:
    if i=='a':
        x+=1
l=len(s)
q=n//l
r=n%l

c=0
for i in range(r):
    if s[i]=='a':
        c+=1

ans= q*x +c
print ( ans)