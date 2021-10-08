# chữ hoa - chữ thường


# hàm xét xem số ký tự nào nhiều hơn
def kt(s):
    h = 0
    t = 0
    for i in s:
        if i.isupper():
           h += 1
        elif i.islower():
            t += 1
    if h > t:
        return True
    else:
        return False
# -------------------------------------

s = input()

if kt(s) == True:
    print(s.upper())
else:
    print(s.lower())


