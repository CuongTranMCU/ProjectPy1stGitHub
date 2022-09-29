
Mybook=[
    {"Title":"Android for Development","Author":"Thanh Tran","Publisher":"VNU"},
    {"Title":"Python","Author":"Thanh Tran","Publisher":"VNU"},
    { "Title":"Java","Author":"Pham Dien","Publisher":"SSS" },
    { "Title":"HTML5","Author":"Man Nhi","Publisher":"HCM" },
    { "Title":"Compiler","Author":"Thanh Tran","Publisher":"VNU" },
    { "Title":"C language","Author":"Man Nhi","Publisher":"SSS" },
    { "Title":"Java","Author":"Pham Dien","Publisher":"SSS" },
    { "Title":"PL","Author":"Pham Dien","Publisher":"HCM" }
]
print("Chon de tim kiem:")
print("1.Title")
print("2.Author")
print("3.Publisher")
choice=int(input("Select(1,2,3):"))
while(choice>3 or choice <1):
    choice=int(input("Nhap lai lua chon:"))
key=input("Nhap keyword can tim kiem:")
for i in Mybook:
    if(choice ==1):
        if(i["Title"]==key):
            print(i)
    elif choice==2:
        if(i["Author"]==key):
            print(i)
    else:
        if(i["Publisher"]==key):
            print(i)



