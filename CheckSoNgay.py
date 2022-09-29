def KiemTraNamNhuan(year):
    if( year %4 ==0 and year %100 !=0) or(year %400 ==0 ):
        return True
    else:
         return False
month=int(input("Nhap thang:"))
if month in (1,3,5,7,8,10,12):
    print(f"Thang {month} co 31 ngay")
elif month in(4,6,9,11):
    print(f"Thang {month} co 30 ngay")
else:
    year =int(input("Nhap nam:"))
    if(KiemTraNamNhuan(year)):
        print(f"Thang {month} co 29 ngay:")
    else:
        print(f"Thang {month} co 28 ngay")
