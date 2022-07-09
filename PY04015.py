# LẬP HÓA ĐƠN - 1

class HoaDon:
    def __init__(self, ma, ten, csCu, csMoi):
        self.ma = 'KH%02d' % ma
        self.ten = ten
        self.thanhToan = self.tinhTien(csCu, csMoi)
        
    def tinhTien(self, csCu, csMoi):
        soDien = csMoi - csCu
        phuPhi = 0
        tien = 0
        if soDien > 100:
            phuPhi = 0.05
            tien = (50 * 100 + 50 * 150 + (soDien-100) * 200) * (1 + 0.05)
        elif soDien > 50:
            phuPhi = 0.03
            tien = (50 * 100 + (soDien-50) * 150) * (1 + 0.03)
        else:
            phuPhi = 0.02
            tien = (soDien * 100) * (1 + 0.02)
        return round(tien)
    
    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + str(self.thanhToan)


def main():
    if __name__ == '__main__':
        ds = []
        for i in range(1, int(input())+1):
            o = HoaDon(i, input(), int(input()), int(input()))
            ds.append(o)
        ds = sorted(ds, key = lambda x: x.thanhToan, reverse=True)
        
        print(*ds, sep = '\n', end = '')

main()