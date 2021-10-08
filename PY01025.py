# chèn dấu phấy
n = int(input())

s = ''
if(n < 1000):
    print(n)
else:
    k = n % 1000
    s = str(k).zfill(3)
    n = int(n/1000)
    while n >= 1000:
        k = n % 1000
        k = str(k).zfill(3)
        s = k + ',' + s
        n = int(n/1000)
    if(n > 0):
        s = str(n) + ',' + s
    print(s)