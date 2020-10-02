count=int(input().strip())
for _ in range(count):
    answer=False
    try:
        string=input().strip()
        number=float(string)
        ans=True
        number=int(string)
        answer=False
    except:
        pass
    print(answer)