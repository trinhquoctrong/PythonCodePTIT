# số may mắn -1

n = input()
d = 0
for i in range(len(n)):
    if n[i] == '4' or n[i] == '7':
        d += 1
        if d > 7:
            break

if d == 4 or d == 7:
    print("YES")
else:
    print("NO")