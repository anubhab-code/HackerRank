from collections import Counter
for _ in range(int(input())):
    n, b = int(input()), input().strip()
    c = Counter(b)
    if any(c[x] == 1 for x in c if x != "_"):
        print("NO")
    elif "_" not in c and any(b[i - 1] != b[i] and b[i] != b[i + 1] for i in range(1, n - 1)):
        print("NO")
    else:
        print("YES")