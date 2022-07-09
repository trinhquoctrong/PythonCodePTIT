# BẢNG ĐIỂM

import math

class HocSinh:
    def __init__(self, ma, ten, bangdiem):
        self.ma = 'HS%02d' % ma
        self.ten = ten
        self.diem = self.tinhDiem(bangdiem)
        self.xepLoai = self.XL(self.diem)
    
    def tinhDiem(self, bangdiem):
        diem = float(0)
        for i in range(10):
            if i == 0 or i == 1:
                diem += bangdiem[i] * 2
            else:
                diem += bangdiem[i]
        return round(diem/10/1.2, 1)
        
    def XL(self, diem):
        if diem >= 9:       return 'XUAT SAC'
        elif diem >= 8:     return 'GIOI'
        elif diem >= 7:     return 'KHA'
        elif diem >= 5:     return 'TB'
        else:               return 'YEU'
    
    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + ('%.1f' % self.diem) + ' ' + self.xepLoai
    
    
def main():
    if __name__ == '__main__':
        A = []
        
        for i in range(1, int(input()) + 1):
            ten = input()
            bangdiem = [float(x) for x in input().split()]
            hs = HocSinh(i, ten, bangdiem)
            A.append(hs)
        
        A = sorted(A, key = lambda x : x.diem, reverse=True)
        
        print(*A, sep='\n', end='')
            
main()  
    