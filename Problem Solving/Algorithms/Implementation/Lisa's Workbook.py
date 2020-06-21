n, k = map(int, input().strip().split())

t_list = [int(x) for x in input().strip().split()]

cnt = 0
page = 1
for t in t_list:
    _t = t
    lower = 1
    upper = min(k, _t)
    while _t > 0:
        #print(page, lower, upper, _t)
        if lower <= page <= upper:
            cnt += 1
        _t -= (upper-lower+1)
        lower = upper + 1
        upper += min(k, _t)
        page += 1
print(cnt)