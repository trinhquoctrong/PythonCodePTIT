class ThiSinh:
    def __init__(self, ten, ngaySinh, d1, d2, d3):
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.tongDiem = d1 + d2 + d3
    
    def toString(self):
        return self.ten + ' ' + self.ngaySinh + ' ' + str('%.1f' % self.tongDiem)
    
def main():
    if __name__ == '__main__':
        ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
        print(ts.toString())
        
main()