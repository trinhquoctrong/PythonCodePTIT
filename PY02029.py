# bầu cử

n, n = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1
l = len(dict)
dict = sorted(dict.items(),key = lambda x:x[1], reverse = True)

if l == 1 or dict[l-1][1] == dict[0][1]:
    print('NONE')
else:
    max = dict[0][1]
    value = 0
    for i in range(l):
        if dict[i][1] < max:
            print(dict[i][0])
            break