import sys

S = input().strip()
O = "SOS"*(len(S)//3)

print(sum(1 for i in range(len(S)) if S[i]!=O[i]))