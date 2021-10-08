# tổng liên tiếp
import math

for t in range(int(input())):
    n = int(input())
    count = 0
    if n <= 2 or (n % 2 == 0 and int(math.sqrt(n)+1) <= 2):
        print(count)
        continue
    if n % 2 == 0:
        for i in range(3, int(math.sqrt(n*2)+1)):
            if i % 2 == 1 and n % i == 0:
                count += 1
            elif i % 2 == 0 and n % i != 0:
                if n % i == i // 2:
                    count += 1
        print(count)
    else:
        count = 1
        for i in range(3, int(math.sqrt(n*2)+1)):
            if i % 2 == 1 and n % i == 0:
                count += 1
            elif i % 2 == 0 and n % i != 0:
                if n % i == i // 2:
                    count += 1
        print(count)
