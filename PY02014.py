# biến đổi nguyên tố
import math

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

arrPrime = [2]

for i in range(3, 10008, 2):
    if nto(i):
        arrPrime.append(i)

n = int(input())
a = list(int(i) for i in input().split())
a = set(a)
dem = 0
for x in a:
    if nto(x) == False:
        index = [ n for n,i in enumerate(arrPrime) if i > x ][0]        # tìm vị trí thấp nhất trong mảng mà tại đó arr[index] > x
        k = 0
        if index >= 1:
            k = min(arrPrime[index] - x, x - arrPrime[index-1])
        else:
            k = arrPrime[index] - x
        if dem == 0:
            dem = k
        elif dem > 0 and dem < k:
            dem = k
print(dem)