class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def mul(self):
        b = []
        for i in range(self.m):
            x = []
            for j in range(self.n):
                x.append(self.a[j][i])
            b.append(x)
            
        c = []
        for i in range(self.n):
            x = []
            for j in range(self.n):
                tmp = 0
                for k in range(self.m):
                    tmp += self.a[i][k] * b[k][j]
                x.append(tmp)
            c.append(x)
        
        for i in range(self.n):
            for j in range(self.n):
                print(c[i][j], end = ' ')
            print()
            
def main():
    if __name__ == '__main__':
        for test in range(int(input())):
            a = []
            n, m = map(int, input().split())
            for i in range(n):
                a.append([int(x) for x in input().split()])
            matrix = Matrix(n, m, a)
            matrix.mul()
                
main()