# TÍNH ĐIỂM CHUYÊN CẦN

from typing import Collection


class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.chuyenCan = 10
        
    def setChuyenCan(self, cc):
        self.chuyenCan = cc
        
    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.ten, self.lop, self.chuyenCan)
    
    
def main():
    if __name__ == '__main__':
        ds = []
        map = {}
        n = int(input())
        for t in range(n):
            sv = SinhVien(input(), input(), input())
            ds.append(sv)
            map[sv.ma] = sv
        
        for t in range(n):
            s = input().split()
            dd = [i for i in s[1]]
            cc = 10 - 2 * dd.count('v') - dd.count('m')
            if cc < 0:
                cc = 0
            map[s[0]].setChuyenCan(cc)
        
        for sv in ds:
            print(sv, end = '')
            if sv.chuyenCan == 0:
                print(' KDDK')
            else:
                print()
            
main()