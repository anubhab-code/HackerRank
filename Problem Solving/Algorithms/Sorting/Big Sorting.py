n = int(input().strip())
unsorted = [input().strip() for _ in range(n)]
unsorted = sorted(unsorted, key = lambda s : (len(s), s))
for s in unsorted:
    print(s)