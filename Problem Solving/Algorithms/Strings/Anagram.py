def update(s, side):
    for l in s:
        freq[l] = freq.get(l, 0) + side
for t in range(int(input())):
    freq = {}
    l = input()
    if len(l) % 2:
        print(-1)
    else:
        s1, s2 = l[:len(l) // 2], l[len(l) // 2:]
        update(s1, 1)
        update(s2, -1)
        print(sum(map(abs, freq.values())) // 2)