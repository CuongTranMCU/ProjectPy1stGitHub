# Viêt chương trình in ra số lớn thứ 2, nhỏ thứ 2 và In ra vị trí của nó
l=[111,23,8,24,12,99]
def MaxThu2(l):
    li=[]
    for i in l:
        if(i==max(l)):
            continue
        else:
            li.append(i)
    return max(li)
def ViTriMaxThu2(l):
    j=0
    for i in l:
        if(MaxThu2(l)==i):
            return j
        j+=1
# Loại bỏ phần tử lớn nhất của list đó, rồi lấy phần tử lớn nhất của list vừa mới tạo 
print("So lon thu 2:",MaxThu2(l))
print("Vi tri lon thu 2:",ViTriMaxThu2(l))
def MinThu2(l):
    li=[]
    for i in l:
        if(i==min(l)):
            continue
        else:
            li.append(i)
    return min(li)
def ViTriMinThu2(l):
    j=0
    for i in l:
        if(i==MinThu2(l)):
            return j
        j+=1
    return j
print("So nho thu 2:",MinThu2(l))
print("Vi tri nho thu 2:",ViTriMinThu2(l))



            