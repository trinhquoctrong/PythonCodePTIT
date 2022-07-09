# XỬ LÝ VĂN BẢN

text = ''
while True:
    try:
        text = text + input().lower() + ' '
    except EOFError:
        break  

text = text.replace('?', '.').replace('!', '.').strip()#.replace('\t', ' ')

s = text.split('.')

for i in s:
    ss = i.strip().capitalize().split()
    print(' '.join(ss))
    