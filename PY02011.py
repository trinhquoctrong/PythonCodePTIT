# biến đổi về dãy bằng nhau

n = int(input())
a = list(int(i) for i in input().split())

dem = 0
value = 0
for i in a:
    sum = 0
    for j in a:
        sum += abs(i - j)
    if dem == 0:
        dem = sum
        value = i
    elif dem > sum:
        dem = sum
        value = i
print(dem, value)