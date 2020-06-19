s = input().strip()
t = input().strip()
k = int(input().strip())

ls = len(s)
lt = len(t)

lcp = 0 
while lcp <= ls-1 and lcp <= lt-1 and s[lcp] == t[lcp]:
    lcp += 1

if k >= ls + lt:
    print ("Yes")
elif k >= ls + lt - 2*lcp and (k - ls - lt + 2*lcp)%2 == 0:
    print ("Yes")
else:
    print ("No")