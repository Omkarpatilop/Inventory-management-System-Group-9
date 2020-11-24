from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql
class User_Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Inventory Management')
        self.root.geometry("1600x800")
        self.root.config(bg="White")

        self.usr_id = StringVar()
        self.usr_pass = StringVar()
        self.usr_type = StringVar()

        self.login_frame = LabelFrame(self.root, text = "LOGIN", bg = "WHITE", font =("Arial",22))
        self.login_frame.place(x = 400, y = 200, height = 400, width = 800)

        login_type = Label(self.login_frame, text = "LOGIN AS ",bg = "WHITE", font =("Arial",18)).grid(row = 0, column = 0,padx = 10, pady = 15,sticky="w")

        self.login_as = ttk.Combobox(self.login_frame,textvariable = self.usr_type, font =("Arial",18), width = 43,state = "readonly" , justify = "center")
        self.login_as['values']=("Select","Buyer","Seller")
        self.login_as.grid(row = 0, column = 1,padx = 10, pady = 15,sticky="w")
        self.login_as.current(0)

        login_id = Label(self.login_frame, text = "ID ",bg = "WHITE", font =("Arial",18)).grid(row = 1, column = 0,padx = 10, pady = 15,sticky="w")

        self.login_iden = Entry(self.login_frame, textvariable = self.usr_id, width = 45,bg = "LightGray", font =("Arial",18))
        self.login_iden.grid(row = 1, column = 1,padx = 10, pady = 15,sticky="w")

        login_pass = Label(self.login_frame, text = "Password ",bg = "WHITE", font =("Arial",18)).grid(row = 2, column = 0,padx = 10, pady = 15,sticky="w")

        self.login_passen = Entry(self.login_frame,textvariable =self.usr_pass ,show="*", width = 45,bg = "LightGray", font =("Arial",18))
        self.login_passen.grid(row = 2, column = 1,padx = 10, pady = 15,sticky="w")

        self.login_button = Button(self.login_frame, text  = "LOGIN", font =("Arial",14),bd="0", command = self.ureg_login)
        self.login_button.place(x=275, y = 300, width = 200, height = 50)

        self.forgot = Button(self.login_frame, text  = "Forgot Password",bg="White", bd="0",fg="Red",font =("Arial",11), command = self.ureg_forgotpass)
        self.forgot.place(x=50, y = 230, width = 200, height = 50)

        self.register_button = Button(self.login_frame, text  = "Not Registered? Sign Up", font =("Arial",11),bd="0",bg="White",fg="Blue", command= self.register)
        self.register_button.place(x=65, y = 190, width = 200, height = 35)

        self.back_btn = Button(self.root, text  = "<BACK", font =("Arial",18),bd="0",bg="White",fg="RED", command= self.back)
        self.back_btn.grid(row=0, column=0)





    def add_product(self):
        if self.product_id.get()=="" or self.product_name.get()=="":
            messagebox.showerror("Error","All fields arer required!!")
        else:
            self.total = float(self.product_qty.get())*float(self.product_price.get())

            con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
            cur=con.cursor()
            cur.execute("insert into inventory values(%s,%s,%s,%s,%s,%s)",(self.user_id.get(),self.product_id.get(),self.product_name.get(),self.product_qty.get(),self.product_price.get(),self.total))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success","record has been inserted",parent = self.root3)

    def fetch_data(self): 
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("select product_id,product_name,product_qty,product_price,total from inventory")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.product_id.set("")
        self.product_name.set("")
        self.product_qty.set("")  
        self.product_price.set("") 

    def get_cursor(self,ev):
        cursor_row=self.invent_table.focus()
        content=self.invent_table.item(cursor_row)
        row=content['values']
        self.product_id.set(row[1])
        self.product_name.set(row[2])
        self.product_qty.set(row[3])
        
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("update inventory set product_name=%s,product_qty=%s where product_id=%s",(self.product_name.get(),self.product_qty.get(),self.product_id.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("delete  from inventory where product_id=%s",self.product_id.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self): 
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        if f'{self.search_by.get()}'=='product_id':
            statement=f"select product_id,product_name,product_qty,product_price,total from inventory where product_id='{self.search_txt.get()}'"
        else:
            statement=f"select product_id,product_name,product_qty,product_price,total from inventory where product_name='{self.search_txt.get()}'"
        cur.execute(statement)
        self.invent_table.delete(*self.invent_table.get_children())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END, values=row)
            con.commit()
        con.close()


    def seller(self,id):
        self.root3 = Toplevel()
        self.root3.title("----INVENTORY MANAGEMENT----")
        self.root3.geometry("1600x800+0+0")
        title=Label(self.root3,text="INVENTORY MANAGEMENT",bd=10,relief=SOLID,fg="black",bg="cyan",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        
        #-----------------variables---------
        self.product_id=StringVar()
        self.product_name=StringVar()
        self.product_qty=IntVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.product_price=IntVar()
        self.user_id = StringVar()


        #----------MANAGE FRAME----------
        
        self.manage_frame=Frame(self.root3,bd=5,relief=RIDGE,bg="ivory")
        self.manage_frame.place(x=20,y=100,width=600,height=600)
        m_title=Label(self.manage_frame,text="PRODUCT MANAGEMENT",bg="ivory",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id=Label(self.manage_frame,text="USER ID",bg="ivory",fg="black",font=("times new roman",16,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        self.txt_id=Entry(self.manage_frame,textvariable=self.user_id,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.user_id.set(id)
        self.txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_id=Label(self.manage_frame,text="PRODUCT ID",bg="ivory",fg="black",font=("times new roman",16,"bold"))
        lbl_id.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        self.txt_id=Entry(self.manage_frame,textvariable=self.product_id,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_id.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name=Label(self.manage_frame,text="PRODUCT NAME",bg="ivory",fg="black",font=("times new roman",16,"bold"))
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        self.txt_name=Entry(self.manage_frame,textvariable=self.product_name,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_name.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_qty=Label(self.manage_frame,text=" QUANTITY",bg="ivory",fg="black",font=("times new roman",16,"bold"))
        lbl_qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        self.txt_qty=Entry(self.manage_frame,textvariable=self.product_qty,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_qty.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lbl_price=Label(self.manage_frame,text="PRICE (PER UNIT)",bg="ivory",fg="black",font=("times new roman",16,"bold"))
        lbl_price.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        self.txt_price=Entry(self.manage_frame,textvariable=self.product_price,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_price.grid(row=5,column=1,pady=10,padx=20,sticky="w")

    
        
        #----------BUTTON FRAME----------
        self.btn_frame=Frame(self.manage_frame,bd=5,relief=GROOVE,bg="ivory")
        self.btn_frame.place(x=20,y=450,width=420)

        add_btn=Button(self.btn_frame,text="ADD",width=10,command=self.add_product).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(self.btn_frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(self.btn_frame,text="DeLETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(self.btn_frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        






        #----------DETAILS FRAME----------
        self.details_frame=Frame(self.root3,bd=5,relief=RIDGE,bg="ivory")
        self.details_frame.place(x=640,y=100,width=840,height=600)
        
        lbl_search=Label(self.details_frame,text="SEARCH BY",bg="ivory",fg="black",font=("times new roman",16,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(self.details_frame,textvariable=self.search_by,font=("times new roman",13),state='readonly',width=10)
        combo_search['values']=("product_name","product_id")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        self.txt_search=Entry(self.details_frame,width=15,textvariable=self.search_txt,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        search_btn=Button(self.details_frame,text="SEARCH",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(self.details_frame,text="SHOW ALL",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #-----------table frame---------
        self.table_frame=Frame(self.details_frame,bd=4,relief=RIDGE,bg="ivory")
        self.table_frame.place(x=10,y=70,width=760,height=490)
        
        scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.invent_table=ttk.Treeview(self.table_frame,columns=("PRODUCT ID","PRODUCT NAME","QUANTITY","PRICE","TOTAL"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.invent_table.xview)
        scroll_y.config(command=self.invent_table.yview)
        self.invent_table.heading("PRODUCT ID",text="PRODUCT ID:")
        self.invent_table.heading("PRODUCT NAME",text="PRODUCT NAME:")
        self.invent_table.heading("QUANTITY",text="QUANTITY:")
        self.invent_table.heading("PRICE",text="PRICE:")
        self.invent_table.heading("TOTAL",text="TOTAL:")
        self.invent_table['show']='headings'
        self.invent_table.column("PRODUCT ID",width=70)
        self.invent_table.column("PRODUCT NAME",width=200)
        self.invent_table.column("QUANTITY",width=150)
        self.invent_table.column("PRICE",width=150)
        self.invent_table.column("TOTAL",width=150)

        self.invent_table.pack(fill=BOTH,expand=1)
        self.invent_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()

    

    def back(self):
        self.root.destroy()
        import GUI

    def new_password(self):
        if self.usrnew_iden.get() =="" or self.answeren.get() =="" or self.usrnew_passen.get() =="":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root2)
        else:
            try:
                con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Inventory")
                cur = con.cursor()
                keys = "SELECT mail_id, que, answer , password FROM USERS"
                cur.execute(keys)
                for (mail_id,que,answer,password) in cur:
                    if self.usrnew_iden.get() ==mail_id and self.answeren.get() ==answer and self.security_combo.get()==que and self.usrnew_passen.get()==password:
                        messagebox.showinfo("Info","Same password as before",parent = self.root2)
                        self.root2.destroy()
                    elif self.usrnew_iden.get() ==mail_id and self.answeren.get() ==answer and self.security_combo.get()==que:
                        update = "UPDATE USERS SET password=%s WHERE mail_id = %s  "
                        value = (self.usrnew_passen.get(),self.usrnew_iden.get())
                        cur.execute(update,value)
                        messagebox.showinfo("Success","Password changed successfull",parent = self.root2)
                        self.root2.destroy()
                    else:
                        messagebox.showerror("Error","Invalid Credentials",parent = self.root2)
                        self.usrnew_iden.delete(0,END)
                        self.answeren.delete(0,END)
                        self.usrnew_passen.delete(0,END)

                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"{es}",parent = self.root2)
                self.usrnew_iden.delete(0,END)
                self.answeren.delete(0,END)
                self.usrnew_passen.delete(0,END)
    
    def ureg_login(self):
        if self.usr_id.get() =="" or self.usr_pass.get() =="":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root)
        else:
            #try:
            con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Inventory")
            cur = con.cursor()
            select = "SELECT mail_id,password FROM USERS"
            cur.execute(select)
            for (mail_id,password) in cur:
                if self.usr_id.get()==mail_id and self.usr_pass.get()==password:
                    login = TRUE
                    break
                else:
                    login = FALSE
                    break
            if login == TRUE:
                if self.usr_type.get() == "Seller":
                        self.seller(self.usr_id.get())
            elif login == FALSE:
                messagebox.showerror("Error","Invalid Credentials",parent = self.root)
                self.usr_pass.set('')
                self.usr_id.set('')
                
            con.commit()
            con.close()
            #except Exception as es:
                #messagebox.showerror("Error",f"{es}",parent = self.root)
            
    
    def ureg_forgotpass(self):
        self.root2 = Toplevel()
        self.root2.geometry("580x430+550+200")
        self.root2.config(bg="White")
        self.root2.focus_force()
        self.root2.grab_set()
        for_label = Label(self.root2, text = "FORGOT PASSWORD", font =("Arial",20),bg="White")
        for_label.place(x=155 ,y=30)
        usrnew_id = Label(self.root2, text = "E-mail id  : ",bg = "White", font =("Arial",16))
        usrnew_id.place(x=10 ,y=100)
        self.usrnew_iden = Entry(self.root2, width = 30, font =("Arial",16),bd = "5")
        self.usrnew_iden.place(x = 175, y = 100)
        security = Label(self.root2, text = "Security Que : ", font =("Arial",16),bg = "White")
        security.place(x=10 ,y=165)
        self.security_combo = ttk.Combobox(self.root2, font =("Arial",16), state = "readonly" , width = 20, justify = "center")
        self.security_combo['values']=("Select","Your favourite book","Your favourite movie","Your best friend")
        self.security_combo.place(x=10 ,y=205)
        self.security_combo.current(0)
        answer = Label(self.root2, text = "Answer    : ", font =("Arial",16),bg = "White",bd = "5")
        answer.place(x=290 ,y=165)
        self.answeren = Entry(self.root2, width = 20, font =("Arial",16),bd = "5")
        self.answeren.place(x=290 ,y=205)
        usrnew_pass = Label(self.root2, text = "New Password: ", font =("Arial",16),bg = "White")
        usrnew_pass.place(x=10 ,y=280)
        self.usrnew_passen = Entry(self.root2,show = "*", width = 30, font =("Arial",16),bd = "5")
        self.usrnew_passen.place(x=175 ,y=280)
        self.new_pass = Button(self.root2, text  = "Update Password", bd="0",font =("Arial",16), command = new_password)
        self.new_pass.place(x = 200, y = 360)
        

    def register(self):
        self.root.destroy()
        import usrreg

        
        


root = Tk()
obj = User_Login(root)
root.mainloop()
