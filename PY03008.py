# ĐỒ THỊ HÌNH SAO

n = int(input())
dict = {}
for i in range(n-1):
    u, v = map(int, input().split())
    if u not in dict:
        dict[u] = 0
    dict[u] += 1
    if v not in dict:
        dict[v] = 0
    dict[v] += 1

ds = sorted(dict.items(), key = lambda x : x[1], reverse = True)

if ds[0][1] == n-1:
    print('Yes')
else:
    print('No') 