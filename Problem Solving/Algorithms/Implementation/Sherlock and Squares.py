import math

t = int(input())

for n in range(0,t):
    a,b = [int(i) for i in input().strip().split()]
    total = 0
    sqrt_a = math.ceil(math.sqrt(a))
    sqrt_b = math.ceil(math.sqrt(b))
    
    for val in range(sqrt_a, sqrt_b+1):
        if math.pow(val, 2) <= b:
            total += 1
    
    print(total)