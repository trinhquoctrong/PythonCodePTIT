# ĐẾM CẶP ĐỒNG XU

def tohop(n):
    if n < 2:
        return 0
    else:
        return n * (n-1) // 2
        
n = int(input())
hang = {}
cot = {}

for t in range(n):
    x = [i for i in input()]
    hang[t] = x.count('C')
    for i in range(n):
        if i not in cot:
            cot[i] = 0
        if x[i] == 'C':
            cot[i] += 1

cnt = 0
for i in range(n):
    cnt += tohop(hang[i])
    
    cnt += tohop(cot[i])
    
print(cnt)