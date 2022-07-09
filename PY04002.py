class Rectangle:
    def __init__(self, height, width, Color):
        self.height = height
        self.width = width
        self.Color = Color
    
    def perimeter(self):
        return int((self.height + self.width) * 2)

    def area(self):
        return int(self.height * self.width)

    def color(self):
        return self.Color.lower().title()


def Main():
    if __name__ == '__main__':
        arr = input().split()
        if int(arr[0]) <= 0 or int(arr[1]) <= 0:
            print('INVALID')
        else:
            r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
            print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

Main()