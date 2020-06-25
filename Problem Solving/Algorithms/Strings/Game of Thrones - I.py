chars = {}

for c in input():
    if c in chars:
        chars[c] += 1
    else: chars[c] = 1

odds = 0
for c in chars:
    odds += chars[c] % 2
if odds < 2: print("YES")
else: print("NO")