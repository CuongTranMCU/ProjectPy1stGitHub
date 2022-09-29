
n=int(input("Nhap so nguyen:"))
def GiaiThua(n):
    if(n<2):
      return 1
    else:
        return n*GiaiThua(n-1)
print("Giai thua :",GiaiThua(n))


