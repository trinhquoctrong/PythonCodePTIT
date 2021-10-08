# liệt kê các số có hai chữ số tăng dần

s = input()
a = []
for i in range(0, len(s)-len(s)%2, 2):
    a.append(int(s[i]+s[i+1]))
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1
dict = sorted(dict.keys())
for i in dict:
    print(i, end = ' ')
