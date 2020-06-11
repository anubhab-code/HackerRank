return_day, return_month, return_year = [int(e) for e in input().strip().split(' ')]
due_day, due_month, due_year = [int(e) for e in input().strip().split(' ')]


if return_year < due_year:
    print(0)
elif return_year == due_year:
    if return_month < due_month:
        print(0)
    elif return_month == due_month:
        if return_day <= due_day:
            print(0)
        else:
            print(str((return_day - due_day) * 15))
    else:
        print(str((return_month - due_month) * 500))
else:
    print('10000')
