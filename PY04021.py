# TÍNH TOÁN THỜI GIAN

from datetime import datetime

class GameThu:
    def __init__(self, ma, ten, tgVao, tgRa):
        self.ma = ma
        self.ten = ten
        self.tg = self.tinhTG(tgVao, tgRa)
        
    def tinhTG(self, tgVao, tgRa):
        f = '%H:%M'
        return ((datetime.strptime(tgRa, f) - datetime.strptime(tgVao, f)).seconds) / 60
    
    def __str__(self):
        return '%s %s %d gio %d phut' % (self.ma, self.ten, self.tg // 60, self.tg % 60)
    

def main():
    if __name__ == '__main__':
        ds = []
        for i in range(int(input())):
            gameThu = GameThu(input(), input(), input(), input())
            ds.append(gameThu)
            
        ds = sorted(ds, key = lambda x : x.tg, reverse = True)
        
        print(*ds, sep = '\n', end = '')
        
main()