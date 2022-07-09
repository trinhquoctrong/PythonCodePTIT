# BIỂU THỨC

for test in range(int(input())):
    s = input()
    A = []
    for i in s:
        if i == '(' or i == ')':
            A.append(i)
            
    k = 1
    stc = []        # stack
    for i in A:
        if i == '(':
            print(k, end = ' ')
            stc.append(k)
            k += 1
        else:
            print(stc[len(stc)-1], end = ' ')
            stc.pop()
    print()
    