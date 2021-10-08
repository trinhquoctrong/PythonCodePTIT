# số nhỏ nhất còn thiếu

n = int(input())

a = [int(i) for i in input().split()]
a.sort()
k = max(a)+1
for i in range(min(a), max(a)+1):
        if i not in a:
            k = i
            break
print(k)