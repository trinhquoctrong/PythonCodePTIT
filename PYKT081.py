# ĐỊA CHỈ IP

def check(A):
    if len(A) != 4:
        return 'NO'
    for i in A:
        if i.isdigit() == False:
            return 'NO'
        elif int(i) > 255:
            return 'NO'
    return 'YES'

for test in range(int(input())):
    print(check(input().split('.')))