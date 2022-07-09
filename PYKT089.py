# SẮP XẾP CHẴN LẺ

n = int(input())
A = []
while len(A) < n:
    A.extend([int(x) for x in input().split()])
chan = []
le = []

for x in A:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
        
le = sorted(le, reverse=True)
chan = sorted(chan)
i = 0
j = 0
B = []
for x in A:
    if x % 2 == 0:
        B.append(chan[i])
        i += 1
    else:
        B.append(le[j])
        j += 1

print(*B)