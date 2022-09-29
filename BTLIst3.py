# viết chương trình trả về kết quả phép tính
# quest=["2+5+7=","5*10=","sqrt(16)= ","12%2= ","5//2="]
#// lấy phần nguyên , bỏ phần thập phân
# sqrt: import math
from math import sqrt
quest=["2+5+7=","5*10=","sqrt(16)=","12%2=","5//2="]
for i in quest:
    x=float(input(i))
    str=i.strip("=")# xóa dấu =
    ans=eval(str)# tính toàn phép tính cho chuỗi 
    if(x==ans):
        print("True")
    else:
        print("False,Key is ",ans)
#ans=eval(str)# 