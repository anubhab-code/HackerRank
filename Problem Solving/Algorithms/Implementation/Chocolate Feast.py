tests = int(input())
for test in range(tests):
    n, c, m = map(int, input().split())
    ans = n // c
    cur = n // c
    while cur >= m:
        ans += cur // m
        cur = (cur // m) + cur % m
    print(ans)