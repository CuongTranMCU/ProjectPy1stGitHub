# Viết chương trình nhập vào 1 ds list
# 1. Tạo ra 1 list bằng bình phương có phần tử list trước đó
# 2. Đếm có bao nhiêu phần tử trên 50 
n=int(input("Nhap so phan tu:"))
l1=[]
for i in range(n):
    x=int(input(f"l1[{i}]= "))
    l1.append(x)
print(l1)
l2=[]
for i in range(n):
    l2.append(l1[i]**2)
print(l2)
# 2.
dem=0
for i in l2:
    if(i>50):
        dem+=1
print("So phan tu lon hon 50:",dem)
