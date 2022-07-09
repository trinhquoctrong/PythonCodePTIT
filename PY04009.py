# LỚP SỐ PHỨC

from re import L


class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    
    def add(self, p):
        return SoPhuc(self.thuc + p.thuc, self.ao + p.ao)
    
    def mul(self, p):
        return SoPhuc(self.thuc * p.thuc - self.ao * p.ao, self.thuc * p.ao + self.ao * p.thuc)
    
    def __str__(self):
        dau = '+'
        if self.ao < 0:
            dau = '-'
        return '%d %s %di' % (self.thuc, dau, self.ao)
        
def main():
    if __name__ == '__main__':
        for test in range(int(input())):
            a = [int(x) for x in input().split()]
            A = SoPhuc(a[0], a[1])
            B = SoPhuc(a[2], a[3])
            print(A.mul(A.add(B)), end = ', ')
            print((A.add(B)).mul(A.add(B)))
            
main()