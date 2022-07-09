# LẬP HÓA ĐƠN - 3

class HoaDon:
    def __init__(self, ma, ten, soLuong, donGia, chietKhau):
        self.ma = ma
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tongTien = donGia * soLuong - chietKhau
        
    def __str__(self):
        return '%s %s %d %d %d %d' % (self.ma, self.ten, self.soLuong, self.donGia, self.chietKhau, self.tongTien)


def main():
    if __name__ == '__main__':
        ds = []
        for test in range(int(input())):
            hd = HoaDon(input(), input(), int(input()), int(input()), int(input()))
            ds.append(hd)
            
        ds = sorted(ds, key = lambda x : x.tongTien, reverse = True)
        print(*ds, sep = '\n')
        
main()     