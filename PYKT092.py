# ĐIỂM TUYỂN SINH

class ThiSinh:
    def __init__(self, ma, ten, diem, dt, kv):
        self.ma = 'TS%02d' % ma
        self.ten = self.chuanHoaTen(ten)
        self.diem = self.tinhDiem(diem, dt, kv)
        self.kq = self.KQ(self.diem)
        
    def chuanHoaTen(self, ten):
        res = ''
        for i in ten.strip().split():
            res = res + i.title() + ' '
        return res.strip()
        
    def tinhDiem(self, diem, dt, kv):
        diemDT = 0
        diemKV = 0
        if dt != 'Kinh':    diemDT = 1.5
        else:               diemDT = 0
        if kv == '1':       diemKV = 1.5
        elif kv == '2':     diemKV = 1.0
        else:               diemKV = 0
        return diem + diemDT + diemKV
    
    def KQ(self, diem):
        if diem >= 20.5:    return 'Do'
        else:               return 'Truot'
        
    def __str__(self):
        return '%s %s %.1f %s' % (self.ma, self.ten, self.diem, self.kq)
    
def main():
    if __name__ == '__main__':
        ds = []
        for i in range(int(input())):
            ts = ThiSinh(i+1, input(), float(input()), input(), input())
            ds.append(ts)
            
        ds = sorted(ds, key = lambda x : (40 - x.diem, x.ma))
        print(*ds, sep = '\n')
        
main()