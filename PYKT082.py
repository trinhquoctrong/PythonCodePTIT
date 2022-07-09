# TÍNH ĐIỂM THI IELTS

def diem(n):
    if n >= 39:         return 9.0
    elif n >= 37:       return 8.5
    elif n >= 35:       return 8.0
    elif n >= 33:       return 7.5
    elif n >= 30:       return 7.0
    elif n >= 27:       return 6.5
    elif n >= 23:       return 6.0
    elif n >= 20:       return 5.5
    elif n >= 16:       return 5.0
    elif n >= 13:       return 4.5
    elif n >= 10:       return 4.0
    elif n >= 7:        return 3.5
    elif n >= 5:        return 3.0
    elif n >= 3:        return 2.5
    else:               return 0
    
    
def overAll(n):
    if n == int(n):     
        return n
    elif n >= int(n) + 0.25 and n < int(n) + 0.75:      
        return int(n) + 0.5
    elif n >= int(n) + 0.75 and n < int(n) + 1:         
        return int(n) + 1
    else:
        return int(n)
    
for test in range(int(input())):
    A = [float(x) for x in input().split()]
    R = diem(A[0])
    L = diem(A[1])
    S = A[2]
    W = A[3]
    res = overAll((R + L + S + W) / 4)
    print('%.1f' % res)