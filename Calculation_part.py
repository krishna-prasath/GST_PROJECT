def Business_to_Customer():
    x={3907:["Wallets",18],4202:["School Bags",18],8500:["Calculator",18],1704:["Choclates",28],9101:["Watches",28],4203:["Belts",12]}
    temp,lis=0,[]
    hsn=int(input("enter the HSN code"))
    print("product name is ",x[hsn][0])
    price=int(input("Price per Product"))
    qty=int(input("Enter QTY"))
    temp=price*qty
    print("taxable value",temp)
    print("the percentage is ",x[hsn][1])
    print("CGST:",(str(x[hsn][1]//2)+"%"))
    print("SGST:",(str(x[hsn][1]//2)+"%"))
    print("CGST AMT:",((temp*x[hsn][1]//2)/100))
    print("SGST AMT:",((temp*x[hsn][1]//2)/100))
    print("Grant Total:",temp+((temp*x[hsn][1]//2)/100)*2)
def Business_to_Business(GSTN,party_gstn):
    x = {3907: ["Wallets", 18], 4202: ["School Bags", 18], 8500: ["Calculator", 18], 1704: ["Choclates", 28],
         9101: ["Watches", 28], 4203: ["Belts", 12]}
    temp, lis = 0, []
    hsn = int(input("enter the HSN code"))
    print("product name is ", x[hsn][0])
    price = int(input("Price per Product"))
    qty = int(input("Enter QTY"))
    temp = price * qty
    if GSTN[:2]==party_gstn[:2]:
        print("CGST AMT:", ((temp * x[hsn][1] // 2) / 100))
        print("SGST AMT:", ((temp * x[hsn][1] // 2) / 100))
        print("Grant Total:", temp + ((temp * x[hsn][1] // 2) / 100) * 2)
    else:
        print("IGST AMT:", ((temp * x[hsn][1]) / 100))
        print("Grant Total:", temp + ((temp * x[hsn][1]) / 100))


name=input("NAME:")
GSTN=input("GSTN:")
F_Y=input("Finc_year:")
mon=input("Month:")

print("choose 1:B2B or 2:B2C")
sel=input()
if sel=="1":
    print("Enter Party_GSTN")
    p_g=input()
    Business_to_Business(GSTN,p_g)
else:
    Business_to_Customer()

