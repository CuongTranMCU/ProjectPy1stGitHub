
str=input("Nhap chuoi gom chu va so:")
def ChuoiChu(str):
    s=""
    for i in str:
        if(i.isalpha()):
            s=s+i
    return s
def ChuoiSo(str):
    s=""
    for i in str:
        if(i.isdigit()):
            s=s+i
    return s
chuoiChu=ChuoiChu(str)
chuoiSo=ChuoiSo(str)
print("Chuoi chu:",chuoiChu)
print("Chuoi so:",chuoiSo)
