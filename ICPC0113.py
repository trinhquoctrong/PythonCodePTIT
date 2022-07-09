# EMIRP NUMBER

sang = [True] * 1000000002
prime = []
sang[0] = sang[1] = False
i = 2
while i * i <= 1000000001:
    if sang[i] == True:
        prime.append(i)
        for j in range(i*i, 1000000001, i):
            sang[j] = False
    i += 1
