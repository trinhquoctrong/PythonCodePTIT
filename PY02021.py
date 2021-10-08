# dãy con chung của ba dãy số

for t in range(int(input())):
    n1, n2, n3 = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    check = False
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2 and k < n3:
        if a[i] == b[j] and a[i] == c[k]:
            print(a[i], end = ' ')
            check = True
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j] or a[i] < c[k]:
            i += 1
        elif b[j] < a[i] or b[j] < c[k]:
            j += 1
        elif c[k] < a[i] or c[k] < b[j]:
            k += 1
    if check == False:
        print('NO', end = ' ')
    print()
    