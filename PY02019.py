# nguyên tố cùng nhau

def Nto(a, b):
    while b > 0:
        c = b
        b = a % b
        a = c
    if a == 1:
        return True
    else:
        return False

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(n-1):
    for j in range(i+1, n):
        if Nto(a[i], a[j]) == True:
            print(a[i], a[j]) 
