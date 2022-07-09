# TÍNH LƯƠNG

class NhanVien:
    def __init__(self, ma, ten, luongCB, soNgay, dsPhong):
        self.ma = ma
        self.ten = ten
        self.tenPhong = dsPhong[ma[3:5]]
        self.tongLuong = self.tinhLuong(ma, luongCB, soNgay)
    
    def tinhLuong(self, ma, luong, ngay):
        l = ma[0]
        nam = int(ma[1:3])
        heSo = 0
        if l == 'A':
            if nam >= 16:       heSo = 20
            elif nam >= 9:      heSo = 14
            elif nam >= 4:      heSo = 12
            else:               heSo = 10
        elif l == 'B':
            if nam >= 16:       heSo = 16
            elif nam >= 9:      heSo = 13
            elif nam >= 4:      heSo = 11
            else:               heSo = 10
        elif l == 'C':
            if nam >= 16:       heSo = 14
            elif nam >= 9:      heSo = 12
            elif nam >= 4:      heSo = 10
            else:               heSo = 9
        else:
            if nam >= 16:       heSo = 13
            elif nam >= 9:      heSo = 11
            elif nam >= 4:      heSo = 9
            else:               heSo = 8
        return luong * ngay * heSo * 1000
    
    def __str__(self):
        return '%s %s %s %d' % (self.ma, self.ten, self.tenPhong, self.tongLuong)
    
    
def main():
    if __name__ == '__main__':
        dsPhong = {}
        for i in range(int(input())):
            s = input()
            maP = s[0:2]
            tenP = s[2:].strip()
            dsPhong[maP] = tenP
            
        ds = []
        for i in range(int(input())):
            nv = NhanVien(input(), input(), int(input()), int(input()), dsPhong)
            ds.append(nv)
        
        print(*ds, sep = '\n')
       
main() 