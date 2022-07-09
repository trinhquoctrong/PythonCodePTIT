# BẢNG XẾP HẠNG

class SinhVien:
    def __init__(self, ten, nopbai):
        self.ten = ten
        self.nopDung, self.soLanNop = map(int, nopbai.split())
        
    def __str__(self):
        return '{} {} {}'.format(self.ten, self.nopDung, self.soLanNop)
    

def main():
    if __name__ == '__main__':
        ds = []
        for i in range(int(input())):
            sv = SinhVien(input(), input())
            ds.append(sv)
        
        ds = sorted(ds, key = lambda x: (555 - x.nopDung, x.soLanNop, x.ten))
        
        print(*ds, sep = '\n')
        
main()