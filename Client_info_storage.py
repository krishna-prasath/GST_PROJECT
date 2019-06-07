#Database intialization
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="tiger1234",
  database="main")
cur = mydb.cursor()
#funtions to be used
def register():
    print("--------------------Registration---------------------")
    print("To register a New Company enter the Following details")
    gnum=input("GSTN:")
    name=input("Name as per GST Records")
    year=input("Type the FY:")
    mon=input("Type the month of commencemnt:")
    cho=input("Do you want to Submit(y/n)")
    if cho=="y" or cho=="Y":
        sql="insert into register(GST,name,fY,month)values(%s,%s,%s,%s)"
        val=(gnum,name,year,mon)
        cur.execute(sql,val)
        mydb.commit()
    else:
        exit()
def search():
    print("1:Search By GSTN")
    print("2:Search By Name")
    ch=int(input())
    if ch==1:
        se=input("Enter the GSTN:")
        sql="select * from register where GST =%s"
        val=(se,)
        cur.execute(sql,val)
        store=cur.fetchall()
        for i in store:
            print(i)
    else:
        se1 = input("Enter the Name:")
        sql = "select * from register where name =%s"
        val = (se1,)
        cur.execute(sql, val)
        store = cur.fetchall()
        for i in store:
            print(i)
#declaration
var = True
#main screen
print("--------------------------------------------------------------")
print("-------------------------GST:2.0*-----------------------------")
while var == True:
    print("1.REGISTER GSTN")
    print("2.SEARCH GSTN:")
    choice=input()
    if choice=="1":
        register()
    else:
        search()
    print("Do you want to continue(y/n):");a=input()
    if a=="y"or a=="Y":
        pass
    else:
        var=False



