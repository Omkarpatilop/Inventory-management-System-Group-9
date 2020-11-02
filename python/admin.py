from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
class Admin:
    def __init__(self,root):
        self.root = root
        self.root.title('Inventory Management')
        self.root.geometry("1600x800")
        self.root.config(bg="White")

        def admin_login():
            return
        

        def admin_forpass():
            return


        self.adm_frame = LabelFrame(self.root, text ="ADMIN", bg = "White", font =("Arial",20))
        self.adm_frame.place(x = 400, y = 200, height = 400, width = 800)
        adm_id = Label(self.adm_frame, text = "ID            : ", font =("Arial",16)).place(x = 30, y = 80)
        self.adm_iden = Entry(self.adm_frame, width = 45, font =("Arial",16))
        self.adm_iden.place(x = 150, y = 85)
        adm_pass = Label(self.adm_frame, text = "Password : ", font =("Arial",16)).place(x = 30, y = 160)
        self.adm_passen = Entry(self.adm_frame, width = 45, font =("Arial",16))
        self.adm_passen.place(x = 150, y = 165)
        self.adm_login = Button(self.adm_frame, text  = "LOGIN", command = admin_login)
        self.adm_login.place(x=150, y = 250, width = 150, height = 50)
        self.adm_forgot = Button(self.adm_frame, text  = "Forgot Pass", command = admin_forpass)
        self.adm_forgot.place(x=450, y = 250, width = 150, height = 50)

root = Tk()
obj = Admin(root)
root.mainloop()