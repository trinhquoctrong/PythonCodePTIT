# LẬP HÓA ĐƠN - 2

from datetime import datetime

class KhachHang:
    def __init__(self, ma, ten, phong, ngayDen, ngayDi, phatSinh):
        self.ma = 'KH%02d' % ma
        self.ten = ten
        self.phong = phong
        self.soNgay = self.tinhNgay(ngayDen, ngayDi)
        self.thanhTien = self.tinhTien(self.soNgay, phong, phatSinh)
        
    def tinhNgay(self, ngayDen, ngayDi):
        f = '%d/%m/%Y'
        return (datetime.strptime(ngayDi, f) - datetime.strptime(ngayDen, f)).days + 1
    
    def tinhTien(self, ngay, phong, phatSinh):
        tang = int(phong[0])
        gia = 0
        if tang == 1:       gia = 25
        elif tang == 2:     gia = 34
        elif tang == 3:     gia = 50
        else:               gia = 80
        return gia * ngay + phatSinh
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.ten, self.phong, self.soNgay, self.thanhTien)
    
    
def main():
    if __name__ == '__main__':
        ds = []
        for i in range(int(input())):
            kh = KhachHang(i+1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip()))
            ds.append(kh)
            
        ds = sorted(ds, key = lambda x : x.thanhTien, reverse = True)
        print(*ds, sep = '\n', end = '')
        
main()