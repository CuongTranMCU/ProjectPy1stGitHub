D={"21521909":"1876667882","21522764":"11111111","21528234":"22222222","21528342":"34567890"}
tk=input("Nhap tk:")
mk=input("Nhap mk:")
it=D.items()
for i in it:
    if(i[0]==tk):
        if(mk==i[1]):
            print("Login thanh cong")
            quit()
        else:
            print("Mk sai")
            quit()
print("Tk khong ton tai")
# Kiểm tra tk có trong D:
# tk in D 
# Hoặc tk not in D
    