t = int(input())
while t:
    t -= 1
    c = int(input())
    l = int(input())
    prices = [int(x) for x in input().split()]
    found = False
    for i in range(l):
        for j in range(i + 1, l):
            if prices[i] + prices[j] == c:
                found = True
                break
        if found:
            break
    print("{0} {1}".format(i + 1, j + 1))