a="abcdefghijklmnopqrstuvwxyz"
b="zxcvbnmasdfghjklqwertyuiop"
stra=input("Nhap ma a:")
def LayRaThuTu(str,a):
   return a.find(str)
def ConvertToMaB(str,a,b):
    s=""
    for i in str:
        s=s+b[LayRaThuTu(i,a)]
    return s
print("Ma b tu ma a vua nhap:",ConvertToMaB(stra,a,b))



