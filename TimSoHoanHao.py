def DanhSachUoc(n):
    l=[]
    for i in range(1,n):
        if(n%i==0):
            l.append(i)
    return l
def KiemTraSoHoanHao(n):
    li=DanhSachUoc(n)
    tong=0
    for i in li:
        tong=tong+i
    if(tong==n):
        return True
    else:
        return False
for i in range(1,1001):
    if(KiemTraSoHoanHao(i)):
        print(i)
# 6=1+2+3
# 28=1+2+4+7+14



