s = "Hello Proo PTIT   "
s = s.strip()               # bỏ các kí tự trắng (dấu cách) ở đầu và cuối chuỗi
s = s.lower()               # các chữ cái thành chữ thường
s = s.upper()               # các chữ cái thành chữ hoa
s = s.replace('O', 'q')     # thay thế các kí tự 'O' thành 'q'
s = s.swapcase()            # hoa thành thường, thường thành hoa
s = s.title()               # chữ cái đầu viết hoa, còn lại viết thường
list = s.split()            # result:       list = ['Hello, 'Proo', 'PTIT']


q = 'a'
q = q.center(3, '@')        # căn giữa với khoảng cách 2 đầu là 3, bởi các kí tự '@.        result: '@@@a@@@'
q = q.rjust(3, '@')         # căn lề phải       result:     'a@@@'
q = q.ljust(3, '@')         # căn lề trái       result:     '@@@a'