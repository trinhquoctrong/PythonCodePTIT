# PRIME – TRIPLET

m = 1000000
prime = [1] * (m+1)
def sang():
    prime[0] = prime[1] = 0
    for i in range(2, m):
        if prime[i] == 1:
            for j in range(i*i, m, i):
                prime[j] = 0
                
sang()
for test in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n-6):
        if prime[i] == prime[i+2] == prime[i+6] == 1:
            cnt += 1
        elif prime[i] == prime[i+4] == prime[i+6] == 1:
            cnt += 1
    print(cnt)