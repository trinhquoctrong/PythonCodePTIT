# TÁCH NHÓM TỐI ƯU

n, k = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort()
cnt = 1
for i in range(n-1):
    if A[i+1] - A[i] > k:
        cnt += 1

print(cnt)