# TÍNH ĐIỂM TRUNG BÌNH

import math

class SinhVien:
    def __init__(self, ma, ten, d1, d2, d3):
        self.ma = 'SV%02d' % ma
        self.ten = self.chuanHoaTen(ten)
        self.diem = self.tinhDiem(d1, d2, d3)
    
    def chuanHoaTen(self, ten):
        res = ''
        for i in ten.strip().split():
            res = res + i.title() + ' '
        return res.strip()
    
    def tinhDiem(seld, d1, d2, d3):
        diem = (d1 * 3 + d2 * 3 + d3 * 2) / 8
        return math.ceil(diem * 100) / 100
    
    def __str__(self):
        return '%s %s %.2f' % (self.ma, self.ten, self.diem)
    
    
def main():
    if __name__ == '__main__':
        ds = []
        for i in range(int(input())):
            sv = SinhVien(i+1, input(), float(input()), float(input()), float(input()))
            ds.append(sv)
            
        ds = sorted(ds, key = lambda x : x.diem, reverse = True)
        x = 1
        y = 1
        diem = ds[0].diem
        for sv in ds:
            print(sv, end = ' ')
            if sv.diem == diem:
                print(x)
                y += 1
            else:
                x = y
                print(x)
                y += 1
                diem = sv.diem
        
main()