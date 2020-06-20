import sys

N = int(input().strip())
B = [int(B_temp) % 2 for B_temp in input().strip().split(' ')]
cnt = 0
for i in range(N-1):
    if B[i]:
        B[i], B[i+1] = 0, 1 - B[i+1]
        cnt += 2
if B[-1]:
    print('NO')
else:
    print(cnt)