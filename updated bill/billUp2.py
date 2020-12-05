from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import math,random
import pymysql
from datetime import datetime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.resizable(0,0)
        self.root.title("Billing Software")
        bg_titlecolor="navy"
        bg_color="RoyalBlue3"
        title=Label(self.root,bd=12,relief=GROOVE,bg=bg_titlecolor,fg="white",text="Billing Software",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #============ ALL IMAGES ============#
        self.ttotal = ImageTk.PhotoImage(file="F:/mini/biil/button_images/total.png")
        self.Gen_bill=ImageTk.PhotoImage(file="F:/mini/biil/button_images/gen.png")
        self.Clear_b=ImageTk.PhotoImage(file="F:/mini/biil/button_images/clear.png")
        self.inventory_b=ImageTk.PhotoImage(file="F:/mini/biil/button_images/inventory.png")
        self.exit_b=ImageTk.PhotoImage(file="F:/mini/biil/button_images/exit.png")
        self.search_b=ImageTk.PhotoImage(file="F:/mini/biil/button_images/search.png")
        self.add_b=ImageTk.PhotoImage(file="F:/mini/biil/button_images/add.png")
        #=============Variables==================#
        #=========Search Field=============#
        self.search_item_no=StringVar()
        self.search_item_no.set("")

        #========Item Details============#
        self.item_no=StringVar()
        self.item_name=StringVar()
        self.item_price=IntVar()
        self.item_quantity=IntVar()
        self.item_quantity.set(1)

        #===========Customer===========#
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set(str(random.randint(1000,9999)))

        ##-------------Customer Detail Frame-------------##
        F1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,bg=bg_color,fg="white",text="Customer Name",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,textvariable=self.c_name,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,bg=bg_color,fg="white",text="Phone No.",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_lbl=Entry(F1,textvariable=self.c_phon,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,bg=bg_color,fg="white",text="Bill No.",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_lbl=Entry(F1,textvariable=self.search_bill,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 15 bold").grid(row=0,column=6,padx=20,pady=10)

        #============Search Items===============#

        F2=LabelFrame(self.root,bd=10,relief=GROOVE, text="Search Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(y=160,width=325,height=380)

        self.search_name= StringVar()

        item_no_lbl=Label(F2,text="Item Name.",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        combo_search=ttk.Combobox(F2,textvariable=self.search_name,width=15 ,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Item No","Item Name")
        combo_search.grid(row=0,column=1, padx=20,pady=10)

        #==============Button for search using item no.============
        search_no_btn=Button(F2,image=self.search_b,command=self.search_item,bg="RoyalBlue3",text="Search",fg="khaki",pady=10,width=118,bd=0,font="arial 15 bold").grid(row=1,column=1,padx=15,pady=5)
        
        #===============Widgets======================
        F2A=LabelFrame(self.root,bd=10,relief=GROOVE, text="Widgets",font=("times new roman",15,"bold"),fg="orange",bg="snow2")
        F2A.place(x=20,y=370,width=280,height=150)

        btn_inventory=Button(F2A,image=self.inventory_b,command=self.openStock,width=90,height=75,text="INVENTORY",font=("Arial",7,"bold"),compound=TOP,pady=6,bg="snow2",fg="black",bd=5).grid(row=1,column=1,pady=2,padx=12)
        Exit_btn=Button(F2A,image=self.exit_b,command=self.Window_Exit,width=88,height=75,text="EXIT",font=("Arial",7,"bold"),compound=TOP,pady=6,bg="snow2",fg="black",bd=5).grid(row=1,column=2,padx=13,pady=2)
        #============Item Details===============#

        F3=LabelFrame(self.root,bd=10,relief=GROOVE, text="Item Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=160,width=325,height=380)

        g1_lbl=Label(F3,text="Item No:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        g1_txt=Label(F3,textvariable=self.item_no,font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=1,padx=10,pady=10,stick="w")

        g2_lbl=Label(F3,text="Item Name:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=0,pady=10,sticky="w")
        g2_txt=Label(F3,textvariable=self.item_name,font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=1,padx=10,pady=10,stick="w")

        g3_lbl=Label(F3,text="Price:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=0,pady=10,sticky="w")
        g3_txt=Label(F3,textvariable=self.item_price,font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=1,padx=10,pady=10,stick="w")

        item_qty_lbl=Label(F3,text="Item Quantity.",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=0,pady=10,sticky="w")
        item_qty_txt=Entry(F3,width=10,textvariable=self.item_quantity,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        search_name_btn=Button(F3,image=self.add_b,command=self.add_item,bg="sky blue",fg="khaki",pady=15,width=120,bd=0,font="arial 15 bold").grid(row=4,column=1,padx=5,pady=5)


        #============Shopping Cart===============#

        F4=LabelFrame(self.root,bd=10,relief=GROOVE, text="Shopping Cart",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=680,y=160,width=325,height=380)

        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.Stock_Table=ttk.Treeview(F4, column=("item_no","item_name","qty","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("item_no",text="Item No")
        self.Stock_Table.heading("item_name",text="Item Name")
        self.Stock_Table.heading("qty",text="Qty")
        self.Stock_Table.heading("price",text="Price")
        self.Stock_Table['show']='headings'
        self.Stock_Table.column("item_no",width=30)
        self.Stock_Table.column("item_name",width=140)
        self.Stock_Table.column("qty",width=30)
        self.Stock_Table.column("price",width=20)
        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.Stock_Table.bind("<ButtonRelease-1>",self.work_on_focus)

        #=================Bill Area==================#

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=160,width=340,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold", bd=7,relief=GROOVE).pack(fill=X)

        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #================Bottom Frame================#
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F6.place(x=0,y=545,relwidth=1,height=140)

       
        Totallbl = Label(F6,text="Total Bill:", font=("Times",14,"bold"),bg="RoyalBlue3",fg="white")
        Totallbl.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        TotalEntry = Entry(F6,width=10, font=("Times",14,"bold"), bd=5, relief=SUNKEN)
        TotalEntry.grid(row=0,column=1,padx=10,pady=5)

        GSTlbl = Label(F6,text="GST:", font=("Times",14,"bold"),bg="RoyalBlue3",fg="white")
        GSTlbl.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        GSTEntry = Entry(F6,width=10, font=("Times",14,"bold"), bd=5, relief=SUNKEN)
        GSTEntry.grid(row=1,column=1,padx=10,pady=5)

        GrandTotallbl = Label(F6,text="Grand Total:", font=("Times",14,"bold"),bg="RoyalBlue3",fg="white")
        GrandTotallbl.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        GrandTotalEntry = Entry(F6,width=10, font=("Times",14,"bold"), bd=5, relief=SUNKEN)
        GrandTotalEntry.grid(row=0,column=3,padx=10,pady=5)

        CPaylbl = Label(F6,text="Customer Pay:", font=("Times",14,"bold"),bg="RoyalBlue3",fg="white")
        CPaylbl.grid(row=1,column=2,padx=10,pady=5,sticky="w")
        CPayEntry = Entry(F6,width=10, font=("Times",14,"bold"), bd=5, relief=SUNKEN)
        CPayEntry.grid(row=1,column=3,padx=10,pady=5)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=730,width=596,height=105)
        
        #ttotal= Label(btn_F,image =self.ttotal).place(x=50,y=5,width=200,height=50)
        total_btn=Button(btn_F,image=self.ttotal,command=self.find_bill,bg="snow2",text="Total",fg="khaki",pady=12,width=169,bd=0,font="arial 15 bold")
        total_btn.grid(row=0,column=0,padx=12,pady=5)
       
        GBill_btn=Button(btn_F,image=self.Gen_bill,command=self.bill_area,bg="snow2",text="Generate Bill",fg="khaki",pady=12,width=169,bd=0,font="arial 15 bold").grid(row=0,column=1,padx=12,pady=5)
        Clear_btn=Button(btn_F,image=self.Clear_b,command=self.clear,bg="snow2",text="Clear",fg="khaki",pady=12,width=169,bd=0,font="arial 15 bold").grid(row=0,column=2,padx=12,pady=5)
        self.welcome_bill()


    #===============New functions==============

    def search_item(self):
        if self.search_item_no.get()=="":
            messagebox.showerror("Error","No input entered")
            return
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(f"select * from stocks where item_no='{self.search_item_no.get()}'")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Alert","No Item found")
        for row in rows:
            self.item_no.set(row[0])
            self.item_name.set(row[1])
            self.item_price.set(row[3])
        con.commit()
        con.close()

    def add_item(self):

        ###########
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(f"select * from stocks where item_no={self.item_no.get()}")
        rows=cur.fetchall()
        available_quantity=rows[0][2]
        #########




        listOfEntriesInTreeView=self.Stock_Table.get_children()
        for each in listOfEntriesInTreeView:
            if int(self.Stock_Table.item(each)['values'][0])==int(self.item_no.get()):
                new_quantity=int(self.Stock_Table.item(each)['values'][2])+int(self.item_quantity.get())
                if new_quantity<available_quantity or new_quantity==available_quantity:
                    self.Stock_Table.detach(each)
                    new_item=(self.item_no.get(),self.item_name.get(),new_quantity,self.item_price.get()*new_quantity)
                    self.Stock_Table.insert('',END, values=new_item)
                    return
                else:
                    messagebox.showinfo("Alert","Available quantity is less.")
                    return
        if int(self.item_quantity.get())<available_quantity or int(self.item_quantity.get())==available_quantity:
            new_item=(self.item_no.get(),self.item_name.get(),self.item_quantity.get(),self.item_price.get()*self.item_quantity.get())
            self.Stock_Table.insert('',END, values=new_item)

    def bill_area(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        total=0
        if self.c_phon.get()=='' or self.c_name.get()=='':
            messagebox.showinfo("Alert","Enter Customer details first")
            return

        elif self.calculateItemInCart()==0:
            messagebox.showinfo("Alert","Add items to cart")
            return

        self.welcome_bill()
        listOfEntriesInTreeView=self.Stock_Table.get_children()
        i=1

        cur.execute(f"select * from customer where customer_name='{self.c_name.get()}' and customer_phone={self.c_phon.get()}")
        rows=cur.fetchall()
        if len(rows)!=0:
            customer_id=rows[0][0]
        else:
            customer_id=random.randint(1,1000)
            cur.execute(f"insert into customer values ({customer_id},'{self.c_name.get()}',{self.c_phon.get()})")
            con.commit()

        for each in listOfEntriesInTreeView:
            statement=f"insert into sales_stocks values ({self.bill_no.get()},{self.Stock_Table.item(each)['values'][0]},{self.Stock_Table.item(each)['values'][2]})"
            cur.execute(statement)
            con.commit()
            statement=f"update stocks set qty=qty-{self.Stock_Table.item(each)['values'][2]} where item_no={self.Stock_Table.item(each)['values'][0]}"
            cur.execute(statement)
            con.commit()
            total=total+int(self.Stock_Table.item(each)['values'][3])
            self.txtarea.insert(END,f"\n{i}\t{self.Stock_Table.item(each)['values'][1]}\t\t     {self.Stock_Table.item(each)['values'][2]}\t {self.Stock_Table.item(each)['values'][3]}")
            self.Stock_Table.detach(each)
            i=i+1
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\n\t\t     Subtotal Rs. {total}")
        self.txtarea.insert(END,f"\n\t\t     Sales Tax Rs. {0.10*total}")
        self.txtarea.insert(END,"\n---------------------------------------")
        self.txtarea.insert(END,f"\n\t\t\tTotal Rs.  {total+0.10*total}")
        self.txtarea.insert(END,"\n---------------------------------------")
        self.txtarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------Thanks for shopping------------")
        self.save_bill()

        #==============Save the bill to database================

        statement=f"insert into sales_bill values ({self.bill_no.get()},'{datetime.today().strftime('%Y-%m-%d')}',{total+0.1*total},{customer_id}) "
        cur.execute(statement)
        con.commit()
        con.close()

    def save_bill(self):
        self.bill_data=self.txtarea.get('1.0',END)
        f1=open("generated_bill/"+self.bill_no.get()+".txt","w")
        f1.write(self.bill_data)
        f1.close()
        messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} saved Successfully.")

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to My Shop")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\nS.No  \tItem Name\t\t   Qty \tPrice")
        self.txtarea.insert(END,f"\n=======================================")

    def calculateItemInCart(self):
        listOfEntriesInTreeView=self.Stock_Table.get_children()
        i=0
        for each in listOfEntriesInTreeView:
            i=i+1
        return (i)

    def work_on_focus(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_quantity.set(row[2])
        self.item_price.set(row[3])

    def clear(self):
        self.Stock_Table.delete(*self.Stock_Table.get_children())
        self.item_no.set("")
        self.item_name.set("")
        self.item_price.set(0)
        self.item_quantity.set(1)
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set(str(random.randint(1000,9999)))
        self.welcome_bill()

    def find_bill(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(f"select * from sales_bill where inv_id={self.search_bill.get()}")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Not Found",f"Bill No. :{self.search_bill.get()} not found.")
            return
        inv_date=rows[0][1]
        inv_amount=rows[0][2]
        inv_id=rows[0][0]
        cur.execute(f"select * from customer where customer_id={rows[0][3]}")
        rows=cur.fetchall()
        c_name=rows[0][1]
        c_phone=rows[0][2]
        self.txtarea.delete('1.0',END)
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to My Shop")
        self.txtarea.insert(END,f"\n Bill Number: {inv_id}")
        self.txtarea.insert(END,f"\n Bill Date: {inv_date}")
        self.txtarea.insert(END,f"\n Customer Name: {c_name}")
        self.txtarea.insert(END,f"\n Phone Number: {c_phone}")
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\nS.No  \tItem Name\t\t   Qty \tPrice")
        self.txtarea.insert(END,f"\n=======================================")

        cur.execute(f"select * from sales_stocks where inv_id={inv_id}")
        rows=cur.fetchall()
        i=1
        total=0
        for row in rows:
            cur.execute(f"select * from stocks where item_no={row[1]}")
            temp=cur.fetchall()
            self.txtarea.insert(END,f"\n{i}\t{temp[0][1]}\t\t     {row[2]}\t {temp[0][3]}")
            total=total+row[2]*temp[0][3]
            i=i+1
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\n\t\t     Subtotal Rs. {total}")
        self.txtarea.insert(END,f"\n\t\t     Sales Tax Rs. {0.18*total}")
        self.txtarea.insert(END,"\n---------------------------------------")
        self.txtarea.insert(END,f"\n\t\t\tTotal Rs.  {total+0.18*total}")
        self.txtarea.insert(END,"\n---------------------------------------")
        self.txtarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------Thanks for shopping------------")
    
    
    def openStock(self):
        from ims_stock import Stock
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Stock(self.root)
    def Window_Exit(self):
        mes= messagebox.askyesno("Notification","Do You want to close?")    
        if mes > 0:
            self.root.destroy()  


root=Tk()
obb=Bill_App(root)
root.mainloop()

    