# XÁC ĐỊNH TRÚNG TUYỂN

class GiaoVien:
    def __init__(self, ma, ten, maXet, diemTin, diemCM):
        self.ma = 'GV%02d' % ma
        self.ten = ten
        self.mon = self.monHoc(maXet)
        self.tongDiem = self.tinhDiem(maXet, diemTin, diemCM)
        self.kq = self.ketQua(self.tongDiem)
        
    def monHoc(self, maXet):
        if maXet[0] == 'A':     return 'TOAN'
        elif maXet[0] == 'B':   return 'LY'
        else:                   return 'HOA'
        
    def tinhDiem(self, maXet, diemTin, diemCM):
        diemUT = 0
        if maXet[1] == '1':         diemUT = 2.0
        elif maXet[1] == '2':       diemUT = 1.5
        elif maXet[1] == '3':       diemUT = 1.0
        else:                       diemUT = 0
        
        return diemTin * 2 + diemCM + diemUT
    
    def ketQua(self, tongDiem):
        if tongDiem >= 18:      return 'TRUNG TUYEN'
        else:                   return 'LOAI'
        
    def __str__(self):
        return '%s %s %s %s %s' % (self.ma, self.ten, self.mon, ('%.1f' % self.tongDiem), self.kq)
    
    
def main():
    if __name__ == '__main__':
        ds = []
        for i in range(int(input())):
            gv = GiaoVien(i+1, input(), input(), float(input()), float(input()))
            ds.append(gv)
            
        ds = sorted(ds, key = lambda x : x.tongDiem, reverse = True)
        print(*ds, sep = '\n')
        
main()