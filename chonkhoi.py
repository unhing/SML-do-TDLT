def nhapdiem():
    for i in range(len(ten_mon)):
        diem = float(input("Bạn hãy nhập điểm môn " + str(ten_mon[i] + ' ')))
        bang_diem.append(diem)
    return bang_diem


def laydiem(mon):
    return int(bang_diem[ten_mon.index(mon)])


def tongdiem(khoi):
    return laydiem(khoi[0])*2 + laydiem(khoi[1]) + laydiem(khoi[2])


ten_mon = ['Toán', 'Lý', 'Hóa', 'Sinh', 'Văn', 'Anh', 'Sử', 'Địa']
bang_diem = []
nhapdiem()

khoiA = ['Toán', 'Lý', 'Hóa']
khoiB = ['Sinh', 'Toán', 'Hóa']
khoiC = ['Văn', 'Sử', 'Địa']
khoiD = ['Anh', 'Toán', 'Văn']
khoiA1 = ['Toán', 'Lý', 'Anh']
dskhoi = [khoiA, khoiB, khoiC, khoiD, khoiA1]

j = 0
maxdiem = 0
a = 0
for i in range(len(dskhoi)):
    a = tongdiem(dskhoi[i])
    if a > maxdiem:
        maxdiem = a
        j = i
print("Khối phù hợp với bạn là khối ", dskhoi[j], ' với số điểm là: ', a)
