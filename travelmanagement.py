import tkinter
import mysql.connector
from tkinter import messagebox


db=mysql.connector.connect(
        user='root',
        passwd='',
        host='localhost',
        database='travelag'


    )

twindow=None
txtuserid=None
txtpasswd=None
txtuseridins=None
txtpasswdins=None
txtCarcode=None
txtCarname=None
txtCarcompany=None
txtCarprice=None
txtCarcodedel=None
addCarwindow=None
txtenter=None
txtdistance=None
cur=db.cursor()
def logincreator():
    global loginwindow
    global txtuserid
    global txtpasswd
    loginwindow=tkinter.Tk()
    loginwindow.title('Login')
    loginwindow.minsize(500,500)

    lbl=tkinter.Label(loginwindow,text='TRAVEL AGENCY MANAGEMENT SYSTEM')
    lbl.place(x=100,y=10,height=100,width=300)
    
    lbluserid=tkinter.Label(loginwindow,text='USERID')
    lbluserid.place(x=100,y=100,height=30,width=100)

    lblpasswd=tkinter.Label(loginwindow,text='PASSWD')
    lblpasswd.place(x=100,y=140,height=30,width=100)

    txtuserid=tkinter.Entry(loginwindow)
    txtuserid.place(x=210,y=100,height=30,width=100)

    txtpasswd=tkinter.Entry(loginwindow,show='*')
    txtpasswd.place(x=210,y=140,height=30,width=100)
    
    btncalc=tkinter.Button(loginwindow,text='LOGIN',command=loginmatcher)
    btncalc.place(x=210,y=180,height=30,width=100)

def admincloser(): 
    addadminwindow.destroy()
    welcomecreator()
def topener():
    welcomewindow.destroy()
    trans()

def tcloser():
    twindow.destroy()
    welcomecreator()
    
def addadminopener():
    welcomewindow.destroy()
    addadmincreator()

def Carcloser():
    addCarwindow.destroy()
    welcomecreator()

def addCaropener():
    welcomewindow.destroy()
    addCarcreator()

def updcloser():
    updCarwindow.destroy()
    welcomecreator()

def updCaropener():
    welcomewindow.destroy()
    updCarcreator()

def delcloser():
    delCarwindow.destroy()
    welcomecreator()

def delCaropener():
    welcomewindow.destroy()
    delCarcreator()

def welcomecreator():
  global welcomewindow
  welcomewindow=tkinter.Tk()



  welcomewindow.minsize(500,500)
  welcomewindow.title('Welcome')

  btnbackwel=tkinter.Button(welcomewindow,text='LOG OUT',command=welcomecloser)
  btnbackwel.place(x=10,y=10,height=30,width=100)
 
  btnaddadmin=tkinter.Button(welcomewindow,text='Add admin',command=addadminopener)
  btnaddadmin.place(x=50,y=100,height=30,width=100)
  
  btnaddCar=tkinter.Button(welcomewindow,text='Add Car',command=addCaropener)
  btnaddCar.place(x=160,y=100,height=30,width=100)

  btnupdCar=tkinter.Button(welcomewindow,text='Update Car',command=updCaropener)
  btnupdCar.place(x=270,y=100,height=30,width=100)
  
  btndelCar=tkinter.Button(welcomewindow,text='Delete Car',command=delCaropener)
  btndelCar.place(x=380,y=100,height=30,width=100)

  btnviewCar=tkinter.Button(welcomewindow,text='Transaction',command=topener)
  btnviewCar.place(x=200,y=200,height=30,width=100)


def welcomecloser():
    welcomewindow.destroy()
    logincreator()
  
def loginmatcher():
    global cur
    global loginwindow
    userid=txtuserid.get()
    passwd=txtpasswd.get()
    cur.execute("select * from admin where username='"+userid+"' and password='"+passwd+"'")
    result=cur.fetchall()
    count=0
    for x in result:
        count+=1
    if(count>0):
        loginwindow.destroy()
        welcomecreator()
    else:
        messagebox.showinfo("alert","userid or password error")

#window creation

loginwindow=None
welcomewindow=None
#window creation end    

logincreator()

def addadmincreator():
    global addadminwindow
    global txtuseridins
    global txtpasswdins
    addadminwindow=tkinter.Tk()
    addadminwindow.minsize(500,500)
    addadminwindow.title('Add admin ')
    btncloseadm=tkinter.Button(addadminwindow,text='CLOSE',command=admincloser)
    btncloseadm.place(x=10,y=10,height=30,width=100)

    lbluseridins=tkinter.Label(addadminwindow,text='Username')
    lbluseridins.place(x=100,y=100,height=30,width=100)

    lblpasswdins=tkinter.Label(addadminwindow,text='Password')
    lblpasswdins.place(x=100,y=140,height=30,width=100)
    
    txtuseridins=tkinter.Entry(addadminwindow)
    txtuseridins.place(x=210,y=100,height=30,width=100)

    txtpasswdins=tkinter.Entry(addadminwindow)
    txtpasswdins.place(x=210,y=140,height=30,width=100)
    
    btnadd=tkinter.Button(addadminwindow,text='ADD',command=add)
    btnadd.place(x=210,y=260,height=30,width=100)
    
def addCarcreator():
    global addCarwindow
    global txtCarcode
    global txtCarname
    global txtCarcompany
    global txtCarprice
    addCarwindow=tkinter.Tk()
    addCarwindow.minsize(500,500)
    addCarwindow.title('Add Car ')

    btncloseCar=tkinter.Button(addCarwindow,text='CLOSE',command=Carcloser)
    btncloseCar.place(x=10,y=10,height=30,width=100)

    lblCarcode=tkinter.Label(addCarwindow,text='Car ID')
    lblCarcode.place(x=100,y=100,height=30,width=100)
    
    lblCarname=tkinter.Label(addCarwindow,text='Car Name')
    lblCarname.place(x=100,y=140,height=30,width=100)

    lblCarcompany=tkinter.Label(addCarwindow,text=' Car company')
    lblCarcompany.place(x=100,y=180,height=30,width=100)

    lblCarprice=tkinter.Label(addCarwindow,text=' Rate per KM')
    lblCarprice.place(x=100,y=220,height=30,width=100)

    txtCarcode=tkinter.Entry(addCarwindow)
    txtCarcode.place(x=210,y=100,height=30,width=100)

    txtCarname=tkinter.Entry(addCarwindow)
    txtCarname.place(x=210,y=140,height=30,width=100)

    txtCarcompany=tkinter.Entry(addCarwindow)
    txtCarcompany.place(x=210,y=180,height=30,width=100)

    txtCarprice=tkinter.Entry(addCarwindow)
    txtCarprice.place(x=210,y=220,height=30,width=100)

    btnadd=tkinter.Button(addCarwindow,text='ADD',command=Cars)
    btnadd.place(x=210,y=260,height=30,width=100)
    
def updCarcreator():
    global updCarwindow
    global updCarwindow
    global txtCarnameup
    global txtCarcompanyup
    global txtCarpriceup
    global txtCarcodeup

    updCarwindow=tkinter.Tk()
    updCarwindow.minsize(500,500)
    updCarwindow.title('Update Car')
    
    btncloseupd=tkinter.Button(updCarwindow,text='CLOSE',command=updcloser)
    btncloseupd.place(x=10,y=10,height=30,width=100)

    lblCarcodeup=tkinter.Label(updCarwindow,text='Carcode')
    lblCarcodeup.place(x=100,y=100,height=30,width=100)

    lblCarnameup=tkinter.Label(updCarwindow,text='Car Name')
    lblCarnameup.place(x=100,y=140,height=30,width=100)

    lblCarcompanyup=tkinter.Label(updCarwindow,text=' Car company')
    lblCarcompanyup.place(x=100,y=180,height=30,width=100)

    lblCarpriceup=tkinter.Label(updCarwindow,text=' Rate per KM')
    lblCarpriceup.place(x=100,y=220,height=30,width=100)

    txtCarcodeup=tkinter.Entry(updCarwindow)
    txtCarcodeup.place(x=210,y=100,height=30,width=100)

    txtCarnameup=tkinter.Entry(updCarwindow)
    txtCarnameup.place(x=210,y=140,height=30,width=100)

    txtCarcompanyup=tkinter.Entry(updCarwindow)
    txtCarcompanyup.place(x=210,y=180,height=30,width=100)

    txtCarpriceup=tkinter.Entry(updCarwindow)
    txtCarpriceup.place(x=210,y=220,height=30,width=100)
    
    btnupd=tkinter.Button(updCarwindow,text='UPD',command=update)
    btnupd.place(x=210,y=260,height=30,width=100)


def delCarcreator():
    global delCarwindow
    global txtCarcodedel
    delCarwindow=tkinter.Tk()
    delCarwindow.minsize(500,500)
    delCarwindow.title('Delete Car')
    
    btnclosedel=tkinter.Button(delCarwindow,text='close',command=delcloser)
    btnclosedel.place(x=10,y=10,height=30,width=100)

    lblCarcodedel=tkinter.Label(delCarwindow,text='Carcode')
    lblCarcodedel.place(x=100,y=100,height=30,width=100)

    txtCarcodedel=tkinter.Entry(delCarwindow)
    txtCarcodedel.place(x=210,y=100,height=30,width=100)
    
    btndel=tkinter.Button(delCarwindow,text='DEL',command=cut)
    btndel.place(x=210,y=260,height=30,width=100)

def calculate():
    global cur
    global trans
    global txtenter
    global txtdistance
    
    carcode=txtenter.get()
    km=txtdistance.get()
    cur.execute("select rpk from car  where carcode='"+carcode+"'")
    rpkresult=cur.fetchall()
    flag=0
    for x in rpkresult:
      rate=x[0]
      flag=1
    if(flag==1):
      messagebox.showinfo("Bill",(rate*int(km)))
    else:
      messagebox.showinfo("Error","Code does not exists")
        
def trans():
    global twindow
    twindow=tkinter.Tk()
    twindow.title('Transaction Window')
    twindow.minsize(1280,720)
    global cur
    global txtenter
    global txtdistance
    cur.execute('select * from car')
    carresult=cur.fetchall()
    lblcode=tkinter.Label(twindow,text='carcode')
    lblcode.place(x=50,y=50,height=30,width=100)
    lblcname=tkinter.Label(twindow,text='carname')
    lblcname.place(x=160,y=50,height=30,width=100)
    lblccom=tkinter.Label(twindow,text='company')
    lblccom.place(x=270,y=50,height=30,width=100)
    lblrpk=tkinter.Label(twindow,text='rpk')
    lblrpk.place(x=380,y=50,height=30,width=100)
    
    lblenter=tkinter.Label(twindow,text='Enter car id')
    lblenter.place(x=700,y=50,height=30,width=100)
    txtenter=tkinter.Entry(twindow)
    txtenter.place(x=800,y=50,height=30,width=100)
    
    lbldistance=tkinter.Label(twindow,text='Distance')
    lbldistance.place(x=700,y=90,height=30,width=100)
    txtdistance=tkinter.Entry(twindow)
    txtdistance.place(x=800,y=90,height=30,width=100)
    
    btnenter=tkinter.Button(twindow,text='Calculate',command=calculate)
    btnenter.place(x=800,y=130,height=30,width=100)
    btnclt=tkinter.Button(twindow,text='close',command=tcloser)
    btnclt.place(x=10,y=10,height=30,width=100)
    yy=90
    xx=50
    for x in carresult:
        codelabel=tkinter.Label(twindow,text=x[0])
        codelabel.place(x=xx,y=yy,height=30,width=100)
        xx=xx+110

        namelabel=tkinter.Label(twindow,text=x[1])
        namelabel.place(x=xx,y=yy,height=30,width=100)
        xx=xx+110

        comlabel=tkinter.Label(twindow,text=x[2])
        comlabel.place(x=xx,y=yy,height=30,width=100)
        xx=xx+110

        rpklabel=tkinter.Label(twindow,text=x[3])
        rpklabel.place(x=xx,y=yy,height=30,width=100)
        xx=xx+110

        yy=yy+40
        xx=50

def add():
    global addadminwindow
    global cur
    global useridins
    global passwdins
    cur.execute("insert into admin values('"+txtuseridins.get()+"','"+txtpasswdins.get()+"')")
    db.commit()
 
def Cars():
    global addCarwindow
    global cur
    global txtCarcode
    global txtCarname
    global txtCarcompany
    global txtCarprice
    cur.execute("insert into Car values('"+txtCarcode.get()+"','"+txtCarname.get()+"','"+txtCarcompany.get()+"','"+txtCarprice.get()+"')")
    db.commit()
    messagebox.showinfo('add','Car is inserted to the list')

def cut():
    global deladminwindow
    global cur
    global Carcodedel
    cur.execute("Delete from  Car where Carcode='"+txtCarcodedel.get()+"'")
    db.commit()
    messagebox.showinfo('Cut',"Car is deleted ")
    
def update():
    global db
    global cur
    global updCarwindow
    global txtCarnameup
    global txtCarcompanyup
    global txtCarpriceup
    global txtCarcodeup
    cur=db.cursor()
    cur.execute("update car set carname='"+txtCarnameup.get()+"',company='"+txtCarcompanyup.get()+"',rpk='"+txtCarpriceup.get()+"' where carcode='"+txtCarcodeup.get()+"'")
    db.commit()
    messagebox.showinfo('update',"Car is updated")
