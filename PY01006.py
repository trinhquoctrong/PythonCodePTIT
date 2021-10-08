# số may mắn -2

t = int(input())

while t:
    n = input()
    kt = True
    for i in range(len(n)):
        if n[i] != '4' and n[i] != '7':
            kt = False
            break
    if kt == True:
        print("YES")
    else:
        print("NO")
    t -= 1