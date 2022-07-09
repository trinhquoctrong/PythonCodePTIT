# LỚP PHÂN SỐ - 1 - Trịnh Quốc Trọng

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rutgon(self):
        x = gcd(self.tu, self.mau)
        t = int(self.tu / x)
        m = int(self.mau / x)
        return str(t) + '/' + str(m)
    
def main():
    if __name__ == '__main__':
        tu, mau = map(int, input().split())
        ps = PhanSo(tu, mau)
        print(ps.rutgon())
        
main()