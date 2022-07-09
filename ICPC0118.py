# CUNG HOÀNG ĐẠO

def CungHoangDao(d, m):
    if (m == 3 and 21 <= d <= 31) or (m == 4 and 1 <= d <= 19):
        return 'Bach Duong'
    elif (m == 4 and 20 <= d <= 30) or (m == 5 and 1 <= d <= 20):
        return 'Kim Nguu'
    elif (m == 5 and 21 <= d <= 31) or (m == 6 and 1 <= d <= 20):
        return 'Song Tu'
    elif (m == 6 and 21 <= d <= 30) or (m == 7 and 1 <= d <= 22):
        return 'Cu Giai'
    elif (m == 7 and 23 <= d <= 31) or (m == 8 and 1 <= d <= 22):
        return 'Su Tu'
    elif (m == 8 and 23 <= d <= 31) or (m == 9 and 1 <= d <= 22):
        return 'Xu Nu'
    elif (m == 9 and 23 <= d <= 30) or (m == 10 and 1 <= d <= 22):
        return 'Thien Binh'
    elif (m == 10 and 23 <= d <= 31) or (m == 11 and 1 <= d <= 22):
        return 'Thien Yet'
    elif (m == 11 and 23 <= d <= 30) or (m == 12 and 1 <= d <= 21):
        return 'Nhan Ma'
    elif (m == 12 and 22 <= d <= 31) or (m == 1 and 1 <= d <= 19):
        return 'Ma Ket'
    elif (m == 1 and 20 <= d <= 31) or (m == 2 and 1 <= d <= 18):
        return 'Bao Binh'
    elif (m == 2 and 19 <= d <= 29) or (m == 3 and 1 <= d <= 20):
        return 'Song Ngu'
    else:
        return 'Trinh Quoc Trong'

for test in range(int(input())):
    d, m = map(int, input().split())
    print(CungHoangDao(d, m))