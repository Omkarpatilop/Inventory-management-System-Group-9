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
            cur = con.cursor(buffered=True)
            select = "SELECT * FROM USERS WHERE mail_id = %s and password = %s"
            value = (self.usr_id.get(),self.usr_pass.get())
            cur.execute(select,value)
            rows = cur.fetchone()
            # print(rows)
            if rows == NONE:
                messagebox.showerror("Error","Invalid Credentials",parent = self.root)
                self.usr_pass.set('')
                self.usr_id.set('')

            else:
                if self.usr_type.get() == "Seller":
                   self.root.destroy()
                   import supplier1
                   supplier1.run_supplier(self.usr_id.get())
                  
                   


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
