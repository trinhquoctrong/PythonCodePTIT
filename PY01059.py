# tổng chữ số - tích chữ số

t = int(input())
for o in range(t):
    s = input()
    count = 0
    sum = 0
    product = 1
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if int(s[i]) != 0:
                product *= int(s[i])
                count += 1
    print(sum, end = ' ')
    if count:
        print(product)
    else:
        print(0)