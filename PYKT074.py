# GỬI THÔNG BÁO

for test in range(int(input())):
    s = input().split()
    res = ''
    for i in s:
        if len(res) + len(i) > 100:
            break
        res += i + ' '
    print(res.strip())