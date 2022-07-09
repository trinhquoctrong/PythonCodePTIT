# LỊCH THI HỌC KỲ

from datetime import datetime

class LichThi:
    def __init__(self, ma, maMon, tenMon, ngay, gio, nhom):
        self.ma = 'T%03d' % ma
        self.maMon = maMon
        self.tenMon = tenMon
        self.ngay = datetime.strptime(ngay, '%d/%m/%Y')
        self.gio = datetime.strptime(gio, '%H:%M')
        self.nhom = nhom
        
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.ma, self.maMon, self.tenMon, datetime.strftime(self.ngay, '%d/%m/%Y'),
                                      datetime.strftime(self.gio, '%H:%M'), self.nhom)


def main():
    if __name__ == '__main__':
        n, m = map(int, input().split())
        dsMon = {}
        ds = []
        for i in range(n):
            maMon = input()
            tenMon = input()
            dsMon[maMon] = tenMon
        for i in range(m):
            s = input().split()
            lt = LichThi(i+1, s[0], dsMon[s[0]], s[1], s[2], s[3])
            ds.append(lt)
        
        ds = sorted(ds, key = lambda x : (x.ngay, x.gio, x.ma))
        print(*ds, sep = '\n')
        
main()