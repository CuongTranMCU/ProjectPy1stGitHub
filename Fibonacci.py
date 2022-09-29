def F(n):
    if n==0:
        return 0
    elif n<3:
        return 1
    else:
        return F(n-1)+F(n-2)
print(F(8))
# 0 1 1 2 3 5 8 13 21