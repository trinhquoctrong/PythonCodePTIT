# CÂU HỎI THEO CHỦ ĐỀ - 2

n = int(input())
done = False
dict = {}
ds = []
for i in range(n):
    s = input()
    if len(s) == 0:
        done = False
        continue
    
    if done == False:
        done = True
        ds.append(s)
        dict[s] = 0
    else:
        dict[ds[len(ds)-1]] += 1
        
for i in ds:
    print(i, end = ': ')
    print(dict[i])
    