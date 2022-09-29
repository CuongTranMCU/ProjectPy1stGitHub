def Roi(dt,cp):
    return ((dt-cp)/cp)>=0.75
dt=float(input("Nhap doanh thu:"))
cp=float(input("Nhap chi phi:"))
if(Roi(dt,cp)):
    print("Nen dau tu:")
else:
    print("KHong nen dau tu:")
    