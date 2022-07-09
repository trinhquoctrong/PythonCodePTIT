# TÍNH VẬN TỐC

from datetime import datetime


class CuaRo:
    def __init__(self, ten, donVi, tgDich):
        self.ma = self.chuanHoaMa(ten, donVi)
        self.ten = ten
        self.donVi = donVi
        self.vanToc = self.tinhVanToc(tgDich)
        
    def chuanHoaMa(self, ten, donVi):
        res = ''
        for i in donVi.upper().split():
            res = res + i[0]
        for i in ten.upper().split():
            res = res + i[0]
        return res
    
    def tinhVanToc(self, tgDich):
        f = '%H:%M'
        tg = (datetime.strptime(tgDich, f) - datetime.strptime('6:00', f)).seconds / 3600
        return 120 / tg
    
    def __str__(self):
        return '%s %s %s %d Km/h' % (self.ma, self.ten, self.donVi, int(round(self.vanToc)))
    
    
def main():
    if __name__ == '__main__':
        ds = []
        for t in range(int(input())):
            cr = CuaRo(input(), input(), input())
            ds.append(cr)
        
        ds = sorted(ds, key = lambda x : x.vanToc, reverse = True)
        print(*ds, sep = '\n')
        
main()