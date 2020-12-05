from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
root = Tk()
root.title('Inventory Management')
root.geometry("1600x800")

def exit():
    root.destroy()

def admin():
    root.destroy()
    import admin

def user():
    root.destroy()
    import usrlogin
    
# ----------------------------Main Window--------------------------------
#root_img = ImageTk.PhotoImage(Image.open("C:\\Users\\rohan\\Pictures\\proj_main.jpg"))
#img_label = Label(root, image = root_img).place(x=0, y=0, relwidth = 1 ,relheight = 1)
title_label = Label(root, text = "Inventory Management System", font = ("Arial",35))
title_label.place(x = 450, y = 100)
admin_btn = Button(root, text="ADMIN", command=admin)
admin_btn.place(x = 400, y =300, height= 100, width=200 )

user_btn = Button(root, text="USER", command=user)
user_btn.place(x = 900, y =300, height= 100, width=200)

quit_btn = Button(root, text ="EXIT", command = exit)
quit_btn.place(x = 750, y = 700)

root.mainloop()