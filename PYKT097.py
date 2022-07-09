# CHUẨN HÓA CÂU

import re

text = ''
dau = ['.', '!', '?']
while True:
    try:
        s = input().strip()
        if s[len(s)-1] not in dau:
            s += '.'
        s = ' '.join(s.split())
        text += s + ' '
    except EOFError:
        break

# for i in range(4):
#     s = input().strip()
#     if s[len(s)-1] not in dau:
#         s += '.'
#     s = ' '.join(s.split())
#     text += s + ' '

text = text.replace(' .', '.')
text = text.replace(' !', '!')
text = text.replace(' ?', '?')

text = text.replace('.', '. ')
text = text.replace('!', '! ')
text = text.replace('?', '? ')
cau = text.strip().split('  ')
# print(cau)
for i in cau:
    print(' '.join(i.strip().capitalize().split()))
    