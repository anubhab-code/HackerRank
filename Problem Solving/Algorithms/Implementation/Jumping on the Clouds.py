import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i = count = 0 

while i < n - 1: 
    if (i + 2 < n) and c[i + 2] == 0: 
        i += 2 
        count += 1 
    elif (i + 1 < n) and c[i + 1] == 0: 
        i += 1 
        count += 1 
        
print(count) 