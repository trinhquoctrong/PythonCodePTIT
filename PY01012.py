# chèn xâu

s1 = input()
s2 = input()
index = int(input())
l = len(s1)
s = s1[:index-1] + s2 + s1[index-1:]

print(s)
