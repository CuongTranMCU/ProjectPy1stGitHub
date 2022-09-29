str1="English = 78 Science = 83 Math = 68 History = 65"
# Tính tổng các số
# tính trung bình
l=[int(s) for s in str1.split() if s.isdigit()]
count=0
dem=0
for i in l:
    count+=i
    dem+=1
print(count)
print(count/dem)

