# số đảo nguyên tố cùng nhau

def tc(s):
    a = int(s)
    b = int(s[::-1])
    while b > 0:
        c = b
        b = a % b
        a = c
    if a == 1:
        return 'YES'
    else:
        return 'NO'

for t in range(int(input())):
    print(tc(input()))
