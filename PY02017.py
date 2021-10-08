# tần suất lẻ

for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    dict = {}
    for i in a:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    for x in dict:
        if dict.get(x) % 2 == 1:
            print(x)
            break
