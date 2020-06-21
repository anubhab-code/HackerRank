a = input().split(" ")
b = input().split(" ")

if int(b[2]) < int(a[2]):
    fine = 10000
elif (int(b[1]) < int(a[1])) & (int(b[2]) == int(a[2])):
    fine = 500*(int(a[1]) - int(b[1]))
elif (int(b[0]) < int(a[0])) & (int(b[1]) == int(a[1])) & (int(b[2]) == int(a[2])):
    fine = 15*(int(a[0]) - int(b[0]))
else:
    fine = 0
    
print(fine)