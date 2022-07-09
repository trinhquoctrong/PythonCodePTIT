# DANH SÁCH PHIM

from datetime import datetime

class TheLoaiPhim:
    def __init__(self, maTL, tenTL):
        self.maTL = 'TL%03d' % maTL
        self.tenTL = tenTL
        
class Phim:
    def __init__(self, maPH, tenTL, ngayKhoiChieu, tenPH, soTap):
        self.maPhim = 'P%03d' % maPH
        self.tenTL = tenTL
        self.ngayKC = self.KC(ngayKhoiChieu)
        self.tenPhim = tenPH
        self.soTap = soTap
        
    def KC(self, ngayKhoiChieu):
        f = '%d/%m/%Y'
        return datetime.strptime(ngayKhoiChieu, f)
    
    def __str__(self):
        return '%s %s %s %s %d' % (self.maPhim, self.tenTL, self.ngayKC.strftime('%d/%m/%Y'), self.tenPhim, self.soTap)
    
    
def main():
    if __name__ == '__main__':
        m, n = map(int, input().split())
        dsTL = {}
        dsPhim = []
        for i in range(m):
            tl = TheLoaiPhim(i+1, input())
            dsTL[tl.maTL] = tl.tenTL
        
        for i in range(n):
            p = Phim(i+1, dsTL[input()], input(), input(), int(input()))
            dsPhim.append(p)
            
        dsPhim = sorted(dsPhim, key = lambda x : (x.ngayKC, x.tenPhim, 10001-x.soTap))
        print(*dsPhim, sep = '\n')
        
main()