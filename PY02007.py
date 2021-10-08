# chia dư cho 42

a = []
num = 10
while len(a) < 10:
    s = [int(i) for i in input().split()]
    for i in s:
        if(len(a) < 10):
            a.append(int(i)%42)
print(len(set(a)))