def nhapdiem():
    for i in range(a):
        diem = input("Bạn hãy nhập điểm sinh viên thứ " + str(i + 1) + ' theo thứ tự môn học: ').split()
        diemrl = float(input("Bạn hãy nhập đrl sinh viên thứ " + str(i + 1) + ' '))
        drl.append(diemrl)
        bang_diem.append(diem)
    return bang_diem, drl


def nhapmon():
    for i in range(b):
        mon = input("Nhập tên môn: ")
        tin_chi = int(input("Nhập số tín chỉ của môn: "))
        ten_mon.append(mon)
        so_tin_chi.append(tin_chi)
    return ten_mon, so_tin_chi


def laydiem(i, mon):
    return float(bang_diem[i][ten_mon.index(mon)])


def tinhdiem(j):
    tong_tin_chi = 0
    tong_diem = 0
    for i in range(b):
        tong_tin_chi += so_tin_chi[i]
        tong_diem += laydiem(j, ten_mon[i]) * (so_tin_chi[i])
    return float(tong_diem / tong_tin_chi)


def trungbinh():
    cuoi_ki = []
    for j in range(a):
        diem_cuoi_ky = tinhdiem(j) + 0.2 * drl[j]
        cuoi_ki.append(diem_cuoi_ky)
    for i in range(5):
        max_lop = max(cuoi_ki)
        for j in range(a):
            if cuoi_ki[j] == max_lop:
                vi_tri.append(j)
                cuoi_ki[j] = 0
                break
        top_lop.append(max_lop)
    return top_lop, vi_tri


a = int(input("Nhập số sinh viên trong lớp: "))
b = int(input("Nhập số môn học: "))
ten_mon = []
so_tin_chi = []
bang_diem = []
drl = []
top_lop = []
vi_tri = []
nhapmon()
nhapdiem()
trungbinh()

if a >= 5:
    print("Danh sách top 5 lớp: ")
    for i in range(5):
        print("Điểm top " + str(i + 1) + " là ", str(top_lop[i]), "là bạn thứ " + str(vi_tri[i] + 1))
else:
    print("Danh sách top ", a, " lớp: ")
    for i in range(a):
        print("Điểm top " + str(i + 1) + " là ", str(top_lop[i]), "là bạn thứ " + str(vi_tri[i] + 1))
