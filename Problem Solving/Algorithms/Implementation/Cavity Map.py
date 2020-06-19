n = int(input())
m = [list(input()) for _ in range(n)]
nm = [r[:] for r in m]
for r in range(1,n-1):
    for c in range(1,n-1):
        if max(m[r-1][c],m[r+1][c],m[r][c-1],m[r][c+1]) < m[r][c]:
            nm[r][c] = "X"
print("\n".join("".join(l) for l in nm))