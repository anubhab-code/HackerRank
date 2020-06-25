n=int(input())
s=input()
c=set(s)
lmin=0
for el in c:
    for el2 in c:
        if el!=el2:
            l=0
            prev='A'
            good=True
            for i in range(0,len(s)):
                if s[i]==el or s[i]==el2:
                    if prev!=s[i]:
                        l=l+1
                        prev=s[i]
                    else:
                        good=False
                        break
            if good:
                if lmin<l:
                    lmin=l
print(lmin)