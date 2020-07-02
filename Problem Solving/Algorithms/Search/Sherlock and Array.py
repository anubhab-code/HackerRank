cases = int(input())
for _ in range(cases):
    array_size = int(input())
    array = list(map(int,input().split(' ')))
    lhs = 0
    rhs = sum(array)
    exists = False
    for element in array:
        rhs -= element
        if lhs == rhs:
            exists = True
            break
        lhs += element
    if exists:
        print("YES")
    else:
        print("NO")