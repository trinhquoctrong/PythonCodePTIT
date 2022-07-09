# CÂU HỎI THEO CHỦ ĐỀ - 1

n = int(input())
done = False    # đánh dấu xem cái chuỗi đang nhập có thuộc chủ đề hay không
dict = {}       # key là chủ đề, val là số câu hỏi
ds = []         # lưu tên các chủ đề, là key trong dict
for i in range(n):
    s = input()
    if len(s) == 0:
        done = False
        continue
    
    if done == False:
        done = True
        ds.append(s)
        dict[s] = 0
    else:
        dict[ds[len(ds)-1]] += 1
        
for i in ds:
    print(i, end = ': ')
    print(dict[i])
    