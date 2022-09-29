d=[
    {"name":"Tuan","phone":"555-1414","email":"cuong@gmail.com"},
    {"name":"Cuong","phone":"342-3848","email":"fkkgf@gmail.com" },
    {"name":"Tam","phone":"834-3242","email":""},
    {"name":"An","phone":"134-42228","email":"ckkdf@gmail.com"}
]
for i in d:
    phone=i["phone"]
    if(phone[-1]=="8"):# Cuối của chuỗi
        print(i)
for i in d:
    email=i["email"]
    if(email==""):
        print(i)
