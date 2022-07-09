# XÁC ĐỊNH THỂ LOẠI THƠ

n = int(input())
cnt = 0
theTho = 0
ds = []
for i in range(0, n, 2):
    s = input().split()
    p = input()
    if theTho == 2:
        theTho = 0
        continue
    
    if len(s) == 6:
        if theTho != 1:
            theTho = 1
            cnt += 1
            ds.append(theTho)
    else:
        if theTho != 2:
            theTho = 2
            cnt += 1
            ds.append(theTho)
            
print(cnt)
print(*ds, sep = '\n')