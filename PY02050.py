# ĐOẠN LIÊN TIẾP NHỎ HƠN

for test in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    
    stc = []        #stack
    for i in range(n):
        while (len(stc) > 0 and A[i] >= A[stc[len(stc)-1]]):
            stc.pop()
        if len(stc) == 0:
            print(i + 1, end = ' ')
        else:
            print(i -stc[len(stc)-1], end = ' ')
        
        stc.append(i)
    print()
