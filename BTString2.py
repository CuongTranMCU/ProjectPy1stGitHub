## Viết chương trình kiểm tra tính hợp lệ của mk:
# mk có ít 6 kí tự , chứa ít nhất 1 chữ cái,chứa ít nhất 1 số
mk = input("Nhap mk:")
def KTChuCai(mk):
    for i in mk:
        if(i.isalpha()):
            return True
    return False
def KTSo(mk):
    for i in mk:
        if(i.isdigit()):
            return True
    return False
def KTKhoangTrang(mk):
    for i in mk:
        if(i.isspace()):
            return False
    return True
def KTMK(mk):
    if(len(mk)>=6 and KTChuCai(mk) and KTSo(mk) and KTKhoangTrang(mk)):
        return True
    else:
        return False
while(not KTMK(mk)):
    mk=input(" MK khong hop le Nhap lai mk:")
else:
        print("Mk hop le")
MK=input("Nhap mk de dang nhap")
dem=0
while(MK!=mk):
    dem+=1
    MK=input(f"Sai {dem}/5 lan, Nhap lai mk: ")
    if(dem==5):
        print("Khoa dang nhap")
        break
else:
    print("Mk hop le")



        
    

