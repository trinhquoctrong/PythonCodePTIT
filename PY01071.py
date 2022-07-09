# python file

s = input()
n = len(s)
check = True

for i in s:
    if (i >= 'a' and i <= 'z') == False and (i >= 'A' and i <= 'Z') == False and i != '_' and i != '.':
        check = False
        break
    
if s[n-3:n] != '.py':
    check = False
      
if check:
    print('yes')
else:
    print('no')