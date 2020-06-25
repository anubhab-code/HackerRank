def check(A, B):
    dict = {}
    for l in A:
        dict[l] = 1
    for l in B:
        if dict.get(l, 0) == 1:
            return "YES"
    return "NO"

for i in range(int(input())):
    A, B = input(), input()
    print(check(A, B))