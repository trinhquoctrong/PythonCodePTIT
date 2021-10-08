# tích chữ số - tổng chữ số

for t in range(int(input())):
    s = input()
    product = 1
    sum = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) != 0:
                product *= int(s[i])
        else:
            sum += int(s[i])
    print(product, sum)