# HOÁN VỊ NGƯỢC

import itertools

for test in range(int(input())):
    n = int(input())
    a = [str(x) for x in range(1, n+1)]
    res = list(itertools.permutations(a, n))
    res.reverse()
    print(len(res))
    for i in res:
        print(''.join(i), end = ' ')
    print()