def super_digit(x):
    if x//10 == 0:
        return x
    else:
        l = [int(i) for i in str(x)] 
        dsum = sum(l)
        return super_digit(dsum)

n, kk = input().strip().split(' ')
k = int(kk)
p = 0
for d in n:
    p += int(d)*k
print(super_digit(p))