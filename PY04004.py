# LỚP PHÂN SỐ - 2 - Trịnh Quốc Trọng

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def add(self, p):
        T = self.tu * p.mau + self.mau * p.tu
        M = self.mau * p.mau
        x = gcd(T, M)
        t = int(T/x)
        m = int(M/x)
        return str(t) + '/' + str(m)
    
def main():
    if __name__ == '__main__':
        a = input().split()
        p1 = PhanSo(int(a[0]), int(a[1]))
        p2 = PhanSo(int(a[2]), int(a[3]))
        print(p1.add(p2))
        
main()
        
    
