import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

k_rem = [0 for i in range(k)]

for i in a:
    k_rem[i%k] += 1

count = 0
    
if k % 2 == 0:
    for i in range(1, k//2):
        count += max(k_rem[i], k_rem[k-i])
    if k_rem[0] > 0:
        count += 1
    if k_rem[k//2] > 0:
        count += 1
elif k % 2 == 1:
    for i in range(1, (k+1)//2):
        count += max(k_rem[i], k_rem[k-i])
    if k_rem[0] > 0:
        count += 1
        
print(count)