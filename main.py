import Tkinter as tk
from cassandra.cluster import Cluster
import datetime

currentDT = datetime.datetime.now()

cluster = Cluster()
session = cluster.connect('restoapp')

root = tk.Tk() #untuk membuat window
root.title("RestoApp")#untuk membuat title App
root.configure(bg="#9C0C0C")

#membuat frame home
frame = tk.LabelFrame(root, padx=100,pady=100, bg="#9C0C0C")
frame.pack()

myLabel = tk.Label(frame, text="FAMILY ROASTED CHICKEN", font=(None,20), bg="#9C0C0C", fg="white") #untuk membuat label
myLabel.grid(row=1,column=0) #untuk memasukan label ke dalam window


#fungsi login
def login():
    delete_frames()
    framelogin = tk.LabelFrame(root, padx=100,pady=100, bg="#9C0C0C")
    framelogin.pack()

    myLabel = tk.Label(framelogin, text="LOG IN", font=(None,15), bg="#9C0C0C", fg="white") #untuk membuat label
    myLabel.grid(row=0,column=1) #untuk memasukan label ke dalam window

    global e
    e = tk.Entry(framelogin,bg="#F8D55B", width=50)#untuk membuat input entry
    e.insert(0,"Enter Your E-mail")
    e.grid(row=1,column=1)

    global e1
    e1 = tk.Entry(framelogin,bg="#F8D55B", width=50)
    e1.insert(0,"Enter Your Password")
    e1.grid(row=2,column=1)

    def logintomenu():
        if e.get()== "user" and e1.get()== "user":
            framelogin.pack_forget()
            viewitem()
        if e.get()== "admin" and e1.get()== "admin":
            framelogin.pack_forget()
            modifyitem()
        else:
            myLabel = tk.Label(framelogin, text="Anda belum terdaftar",bg="#9C0C0C", fg="white") #untuk membuat label
            myLabel.grid(row=4,column=1) #untuk memasukan label ke dalam window
            
            
    def dblogin():
        cql_command = "INSERT INTO user_by_id_login(id_user,email_user,password_user) VALUES (uuid(),%s,%s)"
        values = (e.get(),e1.get())
        session.execute(cql_command,values)
        print "Finished"

    myButton = tk.Button(framelogin, text="Log In", bg="#FFB900",command=lambda:[logintomenu(),dblogin()], height=1, width=5) #untuk membuat button belom dibuat commandnya
    myButton.grid(row=3,column=2)

    def back():
        framelogin.pack_forget()
        frame.pack()
        
    backButton = tk.Button(framelogin, text="Back", bg="#FFB900",command=back, height=1, width=5)
    backButton.grid(row=3,column=0)


def viewitem():
    delete_frames()
    global framemenu
    framemenu = tk.LabelFrame(root, padx=130,pady=130,bg="#9C0C0C")
    framemenu.pack()

    #membuat label makanan
    myLabel = tk.Label(framemenu, text="Makanan",font=(None,10),bg="#F8D55B",height=1,width=10) #untuk membuat label
    myLabel.grid(row=0,column=0) #untuk memasukan label ke dalam window

    myentry2 = tk.Entry(framemenu,width=50, bg="#FFB900")
    myentry2.insert(0,"Ayam Bakar Satu Ekor (Rp.90.000)")
    myentry2.grid(row=1,column=1)

    myentry3 = tk.Entry(framemenu,width=50, bg="#FFB900")
    myentry3.insert(0,"Ayam Bakar 10 Potong Random (Rp.80.000)")
    myentry3.grid(row=2,column=1)

    myentry4 = tk.Entry(framemenu,width=50, bg="#FFB900")
    myentry4.insert(0,"Ayam Bakar 5 Potong Random (Rp.65.000)")
    myentry4.grid(row=3,column=1)

    myentry5 = tk.Entry(framemenu,width=50, bg="#FFB900")
    myentry5.insert(0,"Nasi (Rp.10.000")
    myentry5.grid(row=4,column=1)

    #fungsi tambah dan kurang
    listtotal = []
    list2 = []
    def addmenu2():
        list2.append(1)
        jumlah2 = str(sum(list2))
        listtotal.append(90000)
        e_1.delete(0,tk.END)
        e_1.insert(0,sum(list2))

    def removemenu2():
        if len(list2) == 0 or sum(list2)==0 :
            myButton2_1 = tk.Button(framemenu, text="-", bg="#FFB900", state="disabled")
        else :
            list2.append(-1)
            minus = str(sum(list2))
            listtotal.append(-90000)
            e_1.delete(0,tk.END)
            e_1.insert(0,sum(list2))


    list3 = []
    def addmenu3():
        list3.append(1)
        jumlah = str(sum(list3))
        listtotal.append(80000)
        e_2.delete(0,tk.END)
        e_2.insert(0,sum(list3))

    def removemenu3():
        if len(list3) == 0 or sum(list3)==0 :
            myButton3_1 = tk.Button(framemenu, text="-", bg="#FFB900", state="disabled")
        else:
            list3.append(-1)
            minus = str(sum(list3))
            listtotal.append(-80000)
            e_2.delete(0,tk.END)
            e_2.insert(0,sum(list3))

    list4 = []
    def addmenu4():
        list4.append(1)
        jumlah = str(sum(list4))
        listtotal.append(65000)
        e_3.delete(0,tk.END)
        e_3.insert(0,sum(list4))

    def removemenu4():
        if len(list4)==0 or sum(list4)==0:
            myButton4_1 = tk.Button(framemenu, text="-", bg="#FFB900", state="disabled")
        else:
            list4.append(-1)
            minus = str(sum(list4))
            listtotal.append(-65000)
            e_3.delete(0,tk.END)
            e_3.insert(0,sum(list4))

    list5 = []
    def addmenu5():
        list5.append(1)
        jumlah = str(sum(list5))
        listtotal.append(10000)
        e_4.delete(0,tk.END)
        e_4.insert(0,sum(list5))

    def removemenu5():
        if len(list5)==0 or sum(list5)==0:
            myButton5_1 = tk.Button(framemenu, text="-", bg="#FFB900", state="disabled")
        else:
            list5.append(-1)
            minus = str(sum(list5))
            listtotal.append(-10000)
            e_4.delete(0,tk.END)
            e_4.insert(0,sum(list5))

    list6 = []
    def addmenu6():
        list6.append(1)
        jumlah = str(sum(list6))
        listtotal.append(8000)
        e_5.delete(0,tk.END)
        e_5.insert(0,sum(list6))
        
    def removemenu6():
        if len(list6)==0 or sum(list6)==0:
            myButton6_1 = tk.Button(framemenu, text="-", bg="#FFB900", state="disabled")
        else:
            list6.append(-1)
            minus = str(sum(list6))
            listtotal.append(-8000)
            e_5.delete(0,tk.END)
            e_5.insert(0,sum(list6))

    list7 = []
    def addmenu7():
        list7.append(1)
        jumlah = str(sum(list7))
        listtotal.append(7000)
        e_6.delete(0,tk.END)
        e_6.insert(0,sum(list7))

    def removemenu7():
        if len(list7)==0 or sum(list7)==0:
            myButton7_1 = tk.Button(framemenu, text="-", bg="#FFB900", state="disabled")
        else:
            list7.append(-1)
            minus = str(sum(list7))
            listtotal.append(-7000)
            e_6.delete(0,tk.END)
            e_6.insert(0,sum(list7))

    #membuat fungsi harga per menu
    def showprice():
        e1.delete(0,tk.END)
        global harga1
        harga1= 90000 * sum(list2)
        e1.insert(0,harga1)

    def showprice2():
        e2.delete(0,tk.END)
        global harga2
        harga2= 80000 * sum(list3)
        e2.insert(0,harga2)
        
    def showprice3():
        e3.delete(0,tk.END)
        global harga3
        harga3= 65000 * sum(list4)
        e3.insert(0,harga3)

    def showprice4():
        e4.delete(0,tk.END)
        global harga4
        harga4= 10000 * sum(list5)
        e4.insert(0,harga4)

    def showprice5():
        e5.delete(0,tk.END)
        global harga5
        harga5= 8000 * sum(list6)
        e5.insert(0,harga5)

    def showprice6():
        e6.delete(0,tk.END)
        global harga6
        harga6= 7000 * sum(list7)
        e6.insert(0,harga6)


    #membuat button makanan
    myButton2 = tk.Button(framemenu, text="+", bg="#FFB900",command=lambda:[addmenu2(),showprice()],height=1, width=3) #untuk membuat button belom dibuat commandnya
    myButton2.grid(row=1,column=2)
    myButton2_1 = tk.Button(framemenu, text="-", bg="#FFB900",command=lambda:[removemenu2(),showprice()],height=1, width=3)
    myButton2_1.grid(row=1,column=3)

    myButton3 = tk.Button(framemenu, text="+", bg="#FFB900",command=lambda:[addmenu3(),showprice2()],height=1, width=3)#untuk membuat button belom dibuat commandnya
    myButton3.grid(row=2,column=2)
    myButton3_1 = tk.Button(framemenu, text="-", bg="#FFB900",command=lambda:[removemenu3(),showprice2()],height=1, width=3)
    myButton3_1.grid(row=2,column=3)

    myButton4 = tk.Button(framemenu, text="+", bg="#FFB900",command=lambda:[addmenu4(),showprice3()],height=1, width=3) #untuk membuat button belom dibuat commandnya
    myButton4.grid(row=3,column=2)
    myButton4_1 = tk.Button(framemenu, text="-", bg="#FFB900",command=lambda:[removemenu4(),showprice3()],height=1, width=3) 
    myButton4_1.grid(row=3,column=3)

    myButton5 = tk.Button(framemenu, text="+", bg="#FFB900",command=lambda:[addmenu5(),showprice4()],height=1, width=3) #untuk membuat button belom dibuat commandnya
    myButton5.grid(row=4,column=2)
    myButton5_1 = tk.Button(framemenu, text="-", bg="#FFB900",command=lambda:[removemenu5(),showprice4()],height=1, width=3) 
    myButton5_1.grid(row=4,column=3)

    #membuat label minuman
    myLabel1 = tk.Label(framemenu, text="Minuman",font=(None,10),bg="#F8D55B",height=1,width=10) #untuk membuat label
    myLabel1.grid(row=5,column=0) #untuk memasukan label ke dalam window

    myentry6 = tk.Entry(framemenu,width=50, bg="#FFB900")
    myentry6.insert(0,"Iced Tea (Rp.8.000)")
    myentry6.grid(row=6,column=1)

    myentry7 = tk.Entry(framemenu,width=50, bg="#FFB900")
    myentry7.insert(0,"Hot Tea (Rp.7.000)")
    myentry7.grid(row=7,column=1)

    #membuat button minuman
    myButton6 = tk.Button(framemenu, text="+", bg="#FFB900",command=lambda:[addmenu6(),showprice5()],height=1, width=3) #untuk membuat button belom dibuat commandnya
    myButton6.grid(row=6,column=2)
    myButton6_1 = tk.Button(framemenu, text="-", bg="#FFB900",command=lambda:[removemenu6(),showprice5()],height=1, width=3)
    myButton6_1.grid(row=6,column=3)

    myButton7 = tk.Button(framemenu, text="+", bg="#FFB900",command=lambda:[addmenu7(),showprice6()],height=1, width=3) #untuk membuat button belom dibuat commandnya
    myButton7.grid(row=7,column=2)
    myButton7_1 = tk.Button(framemenu, text="-", bg="#FFB900",command=lambda:[removemenu7(),showprice6()],height=1, width=3)
    myButton7_1.grid(row=7,column=3)

    #database pesanan
    def dbpesanan():
        cql_command = "INSERT INTO pesanan_by_id(id_pesanan,nama_pesanan,jumlah_pesanan,harga_pesanan,waktu_pesanan) VALUES (uuid(),%s,%s,%s,%s)"
        time = currentDT.strftime("%Y-%m-%d %H:%M:%S")
        if e_1.get()>="1" :
            values1 = (myentry2.get(),int(e_1.get()),int(e1.get()),time)
            session.execute(cql_command,values1)
        if e_2.get()>="1" :
            values2 = (myentry3.get(),int(e_2.get()),int(e2.get()),time)
            session.execute(cql_command,values2)
        if e_3.get()>="1":
            values3 = (myentry4.get(),int(e_3.get()),int(e3.get()),time)
            session.execute(cql_command,values3)
        if e_4.get()>="1":
            values4 = (myentry5.get(),int(e_4.get()),int(e4.get()),time)
            session.execute(cql_command,values4)
        if e_5.get()>="1":
            values5 = (myentry6.get(),int(e_5.get()),int(e5.get()),time)
            session.execute(cql_command,values5)
        if e_6.get()>="1":
            values6 = (myentry7.get(),int(e_1.get()),int(e1.get()),time)
            session.execute(cql_command,values6)
        print "Finished"
    
    #fungsi order now
    def submitdata():
        framemenu.pack_forget()
        frameorder = tk.LabelFrame(root, padx=10,pady=10,bg="#9C0C0C")
        frameorder.pack()

        myLabel = tk.Label(frameorder, text="Data berhasil disubmit!",bg="#9C0C0C",font=(None,10),fg="white") #untuk membuat label
        myLabel.grid(row=0,column=0) #untuk memasukan label ke dalam window

        def back():
            frameorder.pack_forget()
            frame.pack()
        
        backButton = tk.Button(frameorder, text="Back", bg="#FFB900",command=back)
        backButton.grid(row=1,column=0)

    #membuat button order
    myButton_order = tk.Button(framemenu, text="Submit Data", bg="#FFB900",command=lambda:[submitdata(),dbpesanan()],height=3,width=10) 
    myButton_order.grid(row=12,column=6)

    #membuat input fields harga
    e1 = tk.Entry(framemenu, width=20, bg="#FFB900")
    e1.grid(row=1,column=4)
    e2 = tk.Entry(framemenu, width=20, bg="#FFB900")
    e2.grid(row=2,column=4)
    e3 = tk.Entry(framemenu, width=20, bg="#FFB900")
    e3.grid(row=3,column=4)
    e4 = tk.Entry(framemenu, width=20, bg="#FFB900")
    e4.grid(row=4,column=4)
    e5 = tk.Entry(framemenu, width=20, bg="#FFB900")
    e5.grid(row=6,column=4)
    e6 = tk.Entry(framemenu, width=20, bg="#FFB900")
    e6.grid(row=7,column=4)

    def back():
        framemenu.pack_forget()
        frame.pack()
    
    BackButton = tk.Button(framemenu, text="Back", bg="#FFB900",command=back,height=3,width=5)
    BackButton.grid(row=12,column=0)

    #input jumlah pesanan
    e_1 = tk.Entry(framemenu, width=3, bg="#FFB900")
    e_1.grid(row=1,column=5)
    e_2 = tk.Entry(framemenu, width=3, bg="#FFB900")
    e_2.grid(row=2,column=5)
    e_3 = tk.Entry(framemenu, width=3, bg="#FFB900")
    e_3.grid(row=3,column=5)
    e_4 = tk.Entry(framemenu, width=3, bg="#FFB900")
    e_4.grid(row=4,column=5)
    e_5 = tk.Entry(framemenu, width=3, bg="#FFB900")
    e_5.grid(row=6,column=5)
    e_6 = tk.Entry(framemenu, width=3, bg="#FFB900")
    e_6.grid(row=7,column=5)

def modifyitem():
    delete_frames()
    frameadmin = tk.LabelFrame(root, padx=100,pady=100,bg="#9C0C0C")
    frameadmin.pack()

    def lihatmenu():
        frameadmin.pack_forget()
        viewitem()

    def kelolamenu():
        frameadmin.pack_forget()
        framekmenu = tk.LabelFrame(root, padx=100,pady=100,bg="#9C0C0C")
        framekmenu.pack()

        myLab1 = tk.Label(framekmenu, text="Masukkan nama menu yang akan ditambahkan:",anchor="w",bg="#9C0C0C",font=(None,10),fg="white") 
        myLab1.grid(row=0,column=0)
        ent1 = tk.Entry(framekmenu, width=50, bg="#FFB900")
        ent1.grid(row=1,column=0)

        myLab2 = tk.Label(framekmenu, text="Masukkan harga menu:",anchor="w",bg="#9C0C0C",font=(None,10),fg="white")
        myLab2.grid(row=2,column=0)
        ent2 = tk.Entry(framekmenu, width=50, bg="#FFB900")
        ent2.grid(row=3,column=0)

        myLab3 = tk.Label(framekmenu, text="Masukkan nama menu yang akan dihapus:",anchor="w",bg="#9C0C0C",font=(None,10),fg="white")
        myLab3.grid(row=4,column=0)
        ent3 = tk.Entry(framekmenu, width=50, bg="#FFB900")
        ent3.grid(row=5,column=0)

        but1 = tk.Button(framekmenu, text="Add Menu", bg="#FFB900",height=1, width=10) #untuk membuat button belom dibuat commandnya
        but1.grid(row=1,column=1)
        but2 = tk.Button(framekmenu, text="Harga Menu", bg="#FFB900",height=1, width=10)
        but2.grid(row=3,column=1)
        but3 = tk.Button(framekmenu, text="Remove Menu", bg="#FFB900",height=1, width=10)
        but3.grid(row=5,column=1)
        
                
    #button lihat menu
    myButton = tk.Button(frameadmin, text="Lihat Menu",bg="#FFB900",command=lihatmenu, height =3, width=10) #untuk membuat button
    myButton.grid(row=0,column=0, padx=10, pady=5)

    myButton = tk.Button(frameadmin, text="Kelola Menu",bg="#FFB900",command=kelolamenu, height =3, width=10) #untuk membuat button
    myButton.grid(row=1,column=0, padx=10, pady=5)
    

def delete_frames():
    frame.pack_forget()

    
myButton = tk.Button(frame, text="Log In",bg="#FFB900",command=login, height =2, width=7) #untuk membuat button
myButton.grid(row=2,column=0, padx=10, pady=5)

root.mainloop() #untuk run application
