q = int(input())
for i in range(0,q):
    s = input()
    n = len(s)
    yes = 0;
    if(s[0] == '0' or n == 1):
        print("NO")
    else:
        for j in range(1,n//2 + 1):
            pre = s[0:j]
            pos = 1
            nex = str(int(pre)+1)
            j2 = j
            while True:
                if len(nex) > n-j2 or nex[0] == '0':
                    pos = 0
                    break
                if s[j2:j2+len(nex)] == nex:
                    if j2+len(nex) == n:
                        break
                    j2 += len(nex)
                    nex = str(int(nex)+1)
                else:
                    pos = 0
                    break
            if pos == 1:
                print("YES " + pre)
                yes = 1
                break
        if yes == 0:
            print("NO")