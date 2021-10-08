# đầu cuối

for t in range(int(input())):
    n = input()
    l = len(n)
    x1 = n[0] + n[1]
    x2 = n[l-2] + n[l-1]
    if x1 == x2:
        print("YES")
    else:
        print("NO")