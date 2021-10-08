# đổi chỗ các chữ số

for t in range(int(input())):
    a =  list(int(i) for i in input())
    l = len(a)
    if l == 1:
        print(-1)
        continue
    else:
        i = l-2
        while i >= 0 and a[i] <= a[i+1]:
            i -= 1
        if i == -1:
            print(-1)
        else:
            index = i+1
            for j in range(i+1, l):
                if a[j] > a[index] and a[j] < a[i]:
                    index = j
            a[i], a[index] = a[index], a[i]
            
            if a[0] == 0:
                print(-1)
            else:
                for i in a:
                    print(i, end = '')
                print()