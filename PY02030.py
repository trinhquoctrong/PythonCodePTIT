# phân chia nguyên tố
import math

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = input()
a = [int(i) for i in input().split()]
dict = {}
b = []
for i in a:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1

sum1 = 0
sum2 = 0
for i in dict:
    b.append(i)
    sum1 += i

index = 'NOT FOUND'
for i in range(len(b)):
    sum2 += b[i]
    if nto(sum2) and nto(sum1 - sum2):
        index = i
        break
print(index)
