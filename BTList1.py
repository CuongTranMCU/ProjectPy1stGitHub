from random import randrange


n=int(input("Nhap so phan tu:"))
l=[]
for i in range(n):
   l.append(randrange(1,101))
print(l)
# Tạo ra 1 list có n phần tử và n phần tử được tạo ngẫu nhiên trong (1,100)
# randrange(x,y): Tạo ngẫu nhiên trong khoảng x/y
