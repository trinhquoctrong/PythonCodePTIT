from itertools import permutations

res = [''.join(p) for p in permutations(input())]
# res.sort()
print(*res, sep = '\n', end = '')