T = int( input() )
for Ti in range(T):
    words = input().split()
    r = 0
    for w in words:
        mi = len(w)//2
        for li in range(mi):
            ri = len(w) - 1 - li
            r += abs( ord( w[li] ) - ord( w[ri] ) )
            
    print(r)