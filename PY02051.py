# khôi phục dãy số

n = int(input())
b = []
for i in range(n):
    b.append([int(i) for i in input().split()])
if n == 2:
    print(1, end = ' ')
    print(b[0][1] - 1)
else:
    x = int((b[0][1] + b[0][2] + b[1][2]) / 2) - b[1][2]
    for i in range(n):
        if i == 0:
            print(x, end = ' ')
        else:
            print(b[0][i] - x, end = ' ')