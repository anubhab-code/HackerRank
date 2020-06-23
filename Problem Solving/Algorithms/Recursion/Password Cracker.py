T = int(input())
for t in range(T):
   N = int(input())
   pwd = input().split()
   login = input().strip()
   a = [None] * (len(login) + 1)
   a[0] = []
   for i in range(len(login)):
      if a[i] == None: continue
      for p in pwd:
         j = i + len(p)
         if j < len(a) and a[j] == None and login[i:j] == p:
            a[j] = a[i] + [p]
   if a[-1] == None:
      print('WRONG PASSWORD')
   else:
      print(' '.join(a[-1]))