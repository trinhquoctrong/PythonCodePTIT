# số lộc phát đẹp

def tc(n):
    if n[0] == 8 or '888' in n:
        return 'NO'
    for i in n:
        if i != '6' and i != '8':
            return 'NO'
    return 'YES'

print(tc(input()))