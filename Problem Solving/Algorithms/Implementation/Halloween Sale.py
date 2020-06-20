p, d, m, s = input().strip().split(' ')
p, d, m, s = [int(p), int(d), int(m), int(s)]

bought = 0
cost = p
dollarsLeft = s

while True:
    if dollarsLeft < cost:
        break
    else:
        dollarsLeft -= cost
        bought += 1
        cost = max(m,cost-d)

print(bought)