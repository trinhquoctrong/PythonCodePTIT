# KÝ TỰ THỨ K

for i in range(int(input())):
    n,m = map(int, input().split())
    a=[]
    y=""
    for i in range(n):
        x = y+chr(65+i)+y
        y=x
        a.append(x)
    print(a[n-1][m-1])