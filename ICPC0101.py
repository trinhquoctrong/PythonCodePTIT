# THU GỌN DÃY SỐ


n = int(input())
A = [int(x) for x in input().split()]

stc = []
for x in A:
    if len(stc) == 0:
        stc.append(x)
    else:
        if (x + stc[len(stc)-1]) % 2 == 0:
            stc.pop()
        else:
            stc.append(x)
            
print(len(stc))
        