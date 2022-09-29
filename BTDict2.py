dict_01={
    "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
    "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
    "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
    "V":4,"W":4,"X":8,"Y":4,"Z":10
}
key=dict_01.keys()
value=dict_01.values()
for i in key:
    print(i,end=" ")
print()
for i in value:
    print(i,end=" ")
print()
tong=0
for i in value:
    tong=tong+i
print("Tong cac so la:",tong)
s="University of Technology and Education"
str_upper=s.upper()
print(str_upper)
for i in str_upper:
    if(i in dict_01):
        print(dict_01[i],end="")
    else:
        print(" ",end="")
