# ĐIỀN SỐ

for test in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    cnt = 0
    Max = max(A)
    Min = min(A)
    for i in range(Min+1, Max):
        if i not in A:
            cnt += 1
    print(cnt)