# TUYỂN NHÂN VIÊN

class ThiSinh:
    def __init__(self, ma, ten, lt, th):
        self.ma = 'TS%02d' % ma
        self.ten = ten
        self.diemTB = self.tinhDiemTB(lt, th)
        self.XL = self.xepLoai(self.diemTB)
        
    def tinhDiemTB(self, lt, th):
        if lt > 10:     lt = lt / 10.0
        if th > 10:     th = th / 10.0
        return (lt + th) / 2.0
    
    def xepLoai(self, diem):
        if diem > 9.5:      return 'XUAT SAC'
        elif diem >= 8:     return 'DAT'
        elif diem >= 5:     return 'CAN NHAC'
        else:               return 'TRUOT'
        
    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + ('%.2f' % self.diemTB) + ' ' + self.XL
    

def main():
    if __name__ == '__main__':
        ds = []
        for i in range(1, int(input())+1):
            ts = ThiSinh(i, input(), float(input()), float(input()))
            ds.append(ts)
        
        ds = sorted(ds, key = lambda x : x.diemTB, reverse = True)
        print(*ds, sep='\n', end='')


main()