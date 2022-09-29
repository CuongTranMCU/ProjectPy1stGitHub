year = int (input("Nhap nam:"))
def KiemTraNamNhuan(year):
    if( year %4 ==0 and year %100 !=0) or(year %400 ==0 ):
        return True
    else:
         return False
check =KiemTraNamNhuan(year)
if(check ==True):
    print("Nam nhuan:")
else :
    print("Khong phai nam nhuan")