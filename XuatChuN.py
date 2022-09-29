h = int(input("Nhap do dai:"))
for i in range(h):
    for j in range(h):
        if j==0 or j==h-1 or i+j == h-1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()