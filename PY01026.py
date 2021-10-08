# sắp đặt lại xâu ký tự

def tc(s1, s2):
    if len(s1) != len(s2):
        return 'NO'
    a = []
    b = []
    for i in range(len(s1)):
        a.append(s1[i])
        b.append(s2[i])
    a.sort()
    b.sort()

    if a != b:
        return 'NO'
    else:
        return 'YES'

for t in range(1, int(input())+1):
    print('Test ' + str(t) + ': ' + tc(input(), input()))