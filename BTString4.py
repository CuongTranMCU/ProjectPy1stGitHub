a="""
tôi chăm học 
tôi chịu khó
tôi đẹp trai
tôi bỏ học 
tôi nhát nhớm 
tôi xấu trai
"""
l=a.split()
print(l)
def SoChuToi(list):
    dem=0
    for i in list:
        if(i=="tôi"):
            dem+=1
    return dem
print("So chu toi trong string a:",SoChuToi(l))
