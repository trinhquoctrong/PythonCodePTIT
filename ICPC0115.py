# SỐ KRISH

A = [1]
i = 1
for t in range(1, 10):
    i  *= t
    A.append(i)
    
for test in range(int(input())):
    s = input()
    n = 0
    for i in s:
        n += A[int(i)]
    if n == int(s):
        print('Yes')
    else:
        print('No') 