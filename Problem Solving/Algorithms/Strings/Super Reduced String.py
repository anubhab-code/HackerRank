import sys

a = list(input())
changed = True
while changed :
    changed = False
    for i in range(len(a) - 1) :
        if i + 1 < len(a) and a[i] == a[i + 1] :
            changed  = True
            del a[i + 1]
            del a[i]

print("Empty String" if len(a) == 0 else "".join(a))Super Reduced String