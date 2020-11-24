from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_Application:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1278x800+0+0")
        self.root.title("IMS BILL GENERATION")
        self.root.resizable(True,True)
        title=Label(self.root, text="YOUR CART",bg="navy",fg="white",font=("Times",30,"bold"),pady=9,bd=7,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        #=================== Variables =================================

        #=================== Customer Info Variables =================================
        self.CNameVar = StringVar()
        self.CPhoneVar = StringVar()
        self.BillNoVar = StringVar()

        r_bill = random.randint(1000,9999)
        self.BillNoVar.set(r_bill)

        self.BillSearchVar = StringVar()
        #=================== Product Info Variables =================================
        self.pro1Var = IntVar()
        self.pro2Var = IntVar()
        self.pro3Var = IntVar()
        self.pro4Var = IntVar()
        self.pro5Var = IntVar()
        self.pro6Var = IntVar()
        self.pro7Var = IntVar()
        self.pro8Var = IntVar()
        self.pro9Var = IntVar()
        self.pro10Var = IntVar()
        self.pro11Var = IntVar()
        self.pro12Var = IntVar()
        self.pro13Var = IntVar()
        self.pro14Var = IntVar()

        #=================== Bottomframe Info Variables =================================
        self.TotalVar = IntVar()
        self.GSTVar = IntVar()
        self.GrandTotalVar = IntVar()
        self.CPayVar = IntVar()
        self.CReturnVar = IntVar()
        #=================== MAIN WINDOW =============================================  

        #=================== Customer Detail Frame =================================
        CFrame= LabelFrame(self.root, text="Customer Details", bg="RoyalBlue3", fg="goldenrod",bd=5, font=("Times",10,"bold"))
        CFrame.place(x=0,y=75,relwidth=1)

        #===================Customer detail Section Form==================================
        CNamelbl = Label(CFrame,text="Customer Name:", font=("Times",12,"bold"),bg="RoyalBlue3",fg="white")
        CNamelbl.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        CNameEntry = Entry(CFrame,textvariable=self.CNameVar, width=23, font=("Times",12,"bold"), bd=7, relief=SUNKEN)
        CNameEntry.grid(row=0,column=1,padx=10,pady=5)

        CPhonelbl = Label(CFrame,text="Phone Number:", font=("Times",12,"bold"),bg="RoyalBlue3",fg="white")
        CPhonelbl.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        CPhoneEntry = Entry(CFrame,textvariable=self.CPhoneVar, width=23, font=("Times",12,"bold"), bd=7, relief=SUNKEN)
        CPhoneEntry.grid(row=0,column=3,padx=10,pady=5)

        BillNolbl = Label(CFrame,text="Bill Number:", font=("Times",12,"bold"),bg="RoyalBlue3",fg="white")
        BillNolbl.grid(row=0,column=4,padx=10,pady=5,sticky="w")
        BillNoEntry = Entry(CFrame,textvariable=self.BillNoVar, width=23, font=("Times",12,"bold"), bd=7, relief=SUNKEN)
        BillNoEntry.grid(row=0,column=5,padx=10,pady=5)

        BillSearchBtn = Button(CFrame,text="Search", font=("Times",12,"bold"), bg="CadetBlue1")
        BillSearchBtn.grid(row=0,column=6,padx=10,pady=5)
        
        #====================Product Details Frame================================
        PFrame= LabelFrame(self.root, text="Product Section", bg="RoyalBlue3", fg="goldenrod",bd=7,relief=GROOVE, font=("Times",10,"bold"))
        PFrame.place(x=0,y=143,width=760, height=420)
        P1Frame= LabelFrame(self.root, bg="RoyalBlue3", fg="goldenrod",bd=7,relief=GROOVE, font=("Times",10,"bold"))
        P1Frame.place(x=380,y=148,width=460, height=415)
        
        #====================Product Details Widget ================================
        self.ProductList = [
                        
             "--Select One--",
             "Nike Shoes",
            "Puma Shoes",
            "Decathlon Bicycle",
            "Parle-G",
            "Face Wash",
            "Bean Bag",
            "Table Lamp",
            "Apsara pencils",
            "Joystick",
        ]   
        self.ProductOne=StringVar()
        self.ProductOne.set(self.ProductList[0])

        self.ProductTwo=StringVar()
        self.ProductTwo.set(self.ProductList[0])

        self.ProductThree=StringVar()
        self.ProductThree.set(self.ProductList[0])

        self.ProductFour=StringVar()
        self.ProductFour.set(self.ProductList[0])

        self.ProductFive=StringVar()
        self.ProductFive.set(self.ProductList[0])

        self.ProductSix=StringVar()
        self.ProductSix.set(self.ProductList[0])

        self.ProductSeven=StringVar()
        self.ProductSeven.set(self.ProductList[0])

        self.ProductEight=StringVar()
        self.ProductEight.set(self.ProductList[0])

        self.ProductNine=StringVar()
        self.ProductNine.set(self.ProductList[0])

        self.ProductTen=StringVar()
        self.ProductTen.set(self.ProductList[0])

        self.ProductEleven=StringVar()
        self.ProductEleven.set(self.ProductList[0])

        self.ProductTwelve=StringVar()
        self.ProductTwelve.set(self.ProductList[0])

        self.ProductThirteen=StringVar()
        self.ProductThirteen.set(self.ProductList[0])

        self.ProductFourteen=StringVar()
        self.ProductFourteen.set(self.ProductList[0])

        pro1= OptionMenu(PFrame,self.ProductOne,*self.ProductList)
        pro1.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        pro1.config(width=18,font=("Times",12,"bold"))       
        pro1Entry = Entry(PFrame, textvariable=self.pro1Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
   
        pro1Entry.grid(row=0,column=1,padx=10,pady=10)  

        pro2= OptionMenu(PFrame,self.ProductTwo,*self.ProductList)
        pro2.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        pro2.config(width=18,font=("Times",12,"bold"))       
        pro2Entry = Entry(PFrame, textvariable=self.pro2Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro2Entry.grid(row=1,column=1,padx=10,pady=10) 

        pro3= OptionMenu(PFrame,self.ProductThree,*self.ProductList)
        pro3.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        pro3.config(width=18,font=("Times",12,"bold"))       
        pro3Entry = Entry(PFrame, textvariable=self.pro3Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro3Entry.grid(row=2,column=1,padx=10,pady=10) 

        pro4= OptionMenu(PFrame,self.ProductFour,*self.ProductList)
        pro4.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        pro4.config(width=18,font=("Times",12,"bold"))       
        pro4Entry = Entry(PFrame, textvariable=self.pro4Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro4Entry.grid(row=3,column=1,padx=10,pady=10) 

        pro5= OptionMenu(PFrame,self.ProductFive,*self.ProductList)
        pro5.grid(row=4,column=0,pady=10,padx=10,sticky="w")
        pro5.config(width=18,font=("Times",12,"bold"))       
        pro5Entry = Entry(PFrame, textvariable=self.pro5Var, width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro5Entry.grid(row=4,column=1,padx=10,pady=10) 

        pro6= OptionMenu(PFrame,self.ProductSix,*self.ProductList)
        pro6.grid(row=5,column=0,pady=10,padx=10,sticky="w")
        pro6.config(width=18,font=("Times",12,"bold"))       
        pro6Entry = Entry(PFrame, textvariable=self.pro6Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro6Entry.grid(row=5,column=1,padx=10,pady=10) 

        pro7= OptionMenu(PFrame,self.ProductSeven,*self.ProductList)
        pro7.grid(row=6,column=0,pady=10,padx=10,sticky="w")
        pro7.config(width=18,font=("Times",12,"bold"))       
        pro7Entry = Entry(PFrame, textvariable=self.pro7Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro7Entry.grid(row=6,column=1,padx=10,pady=10) 

        pro8= OptionMenu(P1Frame,self.ProductEight,*self.ProductList)
        pro8.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        pro8.config(width=18,font=("Times",12,"bold"))       
        pro8Entry = Entry(P1Frame, textvariable=self.pro8Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro8Entry.grid(row=0,column=1,padx=10,pady=10)      

        pro9= OptionMenu(P1Frame,self.ProductNine,*self.ProductList)
        pro9.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        pro9.config(width=18,font=("Times",12,"bold"))       
        pro9Entry = Entry(P1Frame, textvariable=self.pro9Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro9Entry.grid(row=1,column=1,padx=10,pady=10) 

        pro10= OptionMenu(P1Frame,self.ProductTen,*self.ProductList)
        pro10.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        pro10.config(width=18,font=("Times",12,"bold"))       
        pro10Entry = Entry(P1Frame, textvariable=self.pro10Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro10Entry.grid(row=2,column=1,padx=10,pady=10) 

        pro11= OptionMenu(P1Frame,self.ProductEleven,*self.ProductList)
        pro11.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        pro11.config(width=18,font=("Times",12,"bold"))       
        pro11Entry = Entry(P1Frame, textvariable=self.pro11Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro11Entry.grid(row=3,column=1,padx=10,pady=10) 

        pro12= OptionMenu(P1Frame,self.ProductTwelve,*self.ProductList)
        pro12.grid(row=4,column=0,pady=10,padx=10,sticky="w")
        pro12.config(width=18,font=("Times",12,"bold"))       
        pro12Entry = Entry(P1Frame, textvariable=self.pro12Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro12Entry.grid(row=4,column=1,padx=10,pady=10) 

        pro13= OptionMenu(P1Frame,self.ProductThirteen,*self.ProductList)
        pro13.grid(row=5,column=0,pady=10,padx=10,sticky="w")
        pro13.config(width=18,font=("Times",12,"bold"))       
        pro13Entry = Entry(P1Frame, textvariable=self.pro13Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro13Entry.grid(row=5,column=1,padx=10,pady=10) 

        pro14= OptionMenu(P1Frame,self.ProductFourteen,*self.ProductList)
        pro14.grid(row=6,column=0,pady=10,padx=10,sticky="w")
        pro14.config(width=18,font=("Times",12,"bold"))       
        pro14Entry = Entry(P1Frame, textvariable=self.pro14Var,width=10, font=("Times",10,"bold"), bd=5, relief=SUNKEN)
        pro14Entry.grid(row=6,column=1,padx=10,pady=10) 

        #====================Billing Area Frame===================================
        BillFrame= Frame(self.root,bd=7,relief=GROOVE)
        BillFrame.place( x=760, y=143, width=519, height=420)

        #====================Billing Area Form ===================================
        bill_title = Label(BillFrame,text="Billing Area",bd=5,relief=GROOVE,font=("times",12,"bold"))
        bill_title.pack(side=TOP,fill=X)
        scroll_y = Scrollbar(BillFrame, orient=VERTICAL)
        self.txtarea = Text(BillFrame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        self.welcomebill()       #commit

        #====================Bottom Frame====================================
        BottomFrame= LabelFrame(self.root, text="Bill Menu", bg="RoyalBlue3", fg="goldenrod",bd=7, font=("Times",10,"bold"))
        BottomFrame.place(x=0,y=563,relwidth=1,height=110)

        #====================Calculation widgets ====================================

        Totallbl = Label(BottomFrame,text="Total Bill:", font=("Times",11,"bold"),bg="RoyalBlue3",fg="white")
        Totallbl.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        TotalEntry = Entry(BottomFrame, textvariable=self.TotalVar,width=10, font=("Times",11,"bold"), bd=5, relief=SUNKEN)
        TotalEntry.grid(row=0,column=1,padx=10,pady=5)

        GSTlbl = Label(BottomFrame,text="GST:", font=("Times",11,"bold"),bg="RoyalBlue3",fg="white")
        GSTlbl.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        GSTEntry = Entry(BottomFrame, textvariable=self.GSTVar,width=10, font=("Times",11,"bold"), bd=5, relief=SUNKEN)
        GSTEntry.grid(row=1,column=1,padx=10,pady=5)

        GrandTotallbl = Label(BottomFrame,text="Grand Total:", font=("Times",11,"bold"),bg="RoyalBlue3",fg="white")
        GrandTotallbl.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        GrandTotalEntry = Entry(BottomFrame, textvariable=self.GrandTotalVar,width=10, font=("Times",11,"bold"),bg="chocolate1", bd=5, relief=SUNKEN)
        GrandTotalEntry.grid(row=0,column=3,padx=10,pady=5)

        CPaylbl = Label(BottomFrame,text="Customer Pay:", font=("Times",11,"bold"),bg="RoyalBlue3",fg="white")
        CPaylbl.grid(row=1,column=2,padx=10,pady=5,sticky="w")
        CPayEntry = Entry(BottomFrame, textvariable=self.CPayVar,width=10, font=("Times",11,"bold"), bd=5, relief=SUNKEN)
        CPayEntry.grid(row=1,column=3,padx=10,pady=5)

        CReturnlbl = Label(BottomFrame,text="Customer Return:", font=("Times",11,"bold"),bg="RoyalBlue3",fg="white")
        CReturnlbl.grid(row=0,column=4,padx=10,pady=5,sticky="w")
        CReturnEntry = Entry(BottomFrame, textvariable=self.CReturnVar,width=10, font=("Times",11,"bold"),bg="Khaki", bd=5, relief=SUNKEN)
        CReturnEntry.grid(row=0,column=5,padx=10,pady=5)

        #====================Button Frame====================================
        BtnFrame= Frame(BottomFrame,bd=7,relief=GROOVE)
        BtnFrame.place(x=700,width=565, height=85)

        Totalbtn = Button(BtnFrame, text="TOTAL", font=("Times",11,"bold"), bg="CadetBlue1",pady=9,width=9,bd=7,command=self.total_sum)
        Totalbtn.grid(row=0,column=0,padx=4,pady=9)

        GenBillbtn = Button(BtnFrame, text="GENERATE", font=("Times",11,"bold"), bg="CadetBlue1",pady=9,width=9,bd=7,command=self.gen_bill)
        GenBillbtn.grid(row=0,column=1,padx=4,pady=9)

        ClearBillbtn = Button(BtnFrame, text="CLEAR", font=("Times",11,"bold"), bg="CadetBlue1",pady=9,width=9,bd=7)
        ClearBillbtn.grid(row=0,column=2,padx=4,pady=9)

        Printbtn = Button(BtnFrame, text="PRINT", font=("Times",11,"bold"), bg="CadetBlue1",pady=9,width=9,bd=7)
        Printbtn.grid(row=0,column=3,padx=4,pady=9)

        Exitbtn = Button(BtnFrame, text="EXIT", font=("Times",11,"bold"), bg="CadetBlue1",pady=9,width=9,bd=7,command=self.Window_Exit)
        Exitbtn.grid(row=0,column=4,padx=4,pady=9)
    
    #====================== TOTAL BUTTON Function ===========================================
    def total_sum(self):
        self.proOne= self.pro1Var.get()
        self.proTwo= self.pro2Var.get()
        self.proThree= self.pro3Var.get()
        self.proFour= self.pro4Var.get()
        self.proFive= self.pro5Var.get()
        self.proSix= self.pro6Var.get()
        self.proSeven= self.pro7Var.get()
        self.proEight= self.pro8Var.get()
        self.proNine= self.pro9Var.get()
        self.proTen= self.pro10Var.get()
        self.proEleven= self.pro11Var.get()
        self.proTwelve= self.pro12Var.get()
        self.proThirteen= self.pro13Var.get()
        self.proFourteen= self.pro14Var.get()

        self.totalsum=float(
                              self.proOne*40+
                              self.proTwo+
                              self.proThree+
                              self.proFour+
                              self.proFive+
                              self.proSix+
                              self.proSeven+
                              self.proEight+
                              self.proNine+
                              self.proTen+
                              self.proEleven+
                              self.proTwelve+
                              self.proThirteen+
                              self.proFourteen
                            )


        self.TotalVar.set(str(self.totalsum))
        
        #self.GST_Cal= self.totalsum * (0.18)
        #self.GSTVar.set(str(self.GST_Cal))

        if self.totalsum > 0:
            if self.totalsum <= 5000:
                 self.GST_Cal = self.totalsum*0.05
                 self.GSTVar.set(str(self.GST_Cal))
            elif self.totalsum <= 15000:
                 self.GST_Cal = self.totalsum*0.12
                 self.GSTVar.set(str(self.GST_Cal))
            elif self.totalsum <= 25000:       
                 self.GST_Cal = 0.18 * self.totalsum
                 self.GSTVar.set(str(self.GST_Cal))
            else: 
                 self.GST_Cal = 0.28 * self.totalsum
                 self.GSTVar.set(str(self.GST_Cal))            

        #self.Discountoffer= (self.totalsum)*(0.10) //if 10 perecnt discount is offered
        #self.DiscountVar.set(str(self.Discountoffer))
     
        self.grand_total =     self.totalsum +self.GSTVar.get()  
        self.GrandTotalVar.set(str(self.grand_total)) 

        self.CPaycash= self.grand_total
        self.CPayVar.set(str(self.CPaycash))
        
        #if self.CPaycash != 0:
            #self.cashreturn = self.CPaycash - self.grand_total
            #self.CReturnVar.set(str(self.cashreturn))

        self.cashreturn =  self.grand_total - self.CPaycash
        self.CReturnVar.set(str(self.cashreturn))
                         
         #====================Billing Area all details execution====================================       
    def welcomebill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t \t  Welcome To Fnatic Bill Area\n")
        self.txtarea.insert(END,"\t \t  Phone No: 2201929929\n\n")
        self.txtarea.insert(END,"============================================================\n")   
        self.txtarea.insert(END,f"Bill No: {self.BillNoVar.get()} \n")
        self.txtarea.insert(END,f"Customer Name: {self.CNameVar.get()} \n")
        self.txtarea.insert(END,f"Phone Number:{self.CPhoneVar.get()}\n")
        self.txtarea.insert(END,"============================================================\n")

        self.txtarea.insert(END,"Product Name \t\t\tQTY  \t\tPrice \n\n")

        #self.txtarea.insert(END,"============================================================\n")
        #self.txtarea.insert(END,"\t \t \t     Total: \n")
        #self.txtarea.insert(END,"\t \t \t     GST: \n")
        #self.txtarea.insert(END,"============================================================\n")

        #self.txtarea.insert(END,"============================================================\n")
        #self.txtarea.insert(END,"\t\t\t     Grand Total: \n")

   #====================== Genrate Bill BUTTON Function =========================================== 
    def gen_bill(self):
        if self.CNameVar.get() == "" and self.CPhoneVar.get() == "":
           messagebox.showerror("Error","Name And Phone Number is required!!!")

        elif self.CPhoneVar.get()=="" =="":
             messagebox.showerror("Error"," Phone Number is required!!!")

        elif self.CNameVar.get() ==""=="":
              messagebox.showerror("Error"," Name is required!!!")

        elif self.TotalVar.get()==""=="":
              messagebox.showerror("Error"," No Products Selected!!!")

        else:
            self.welcomebill()
            if self.pro1Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductOne.get()} \t\t\t\t\t {self.pro1Var.get()} \n")

            if self.pro2Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductTwo.get()} \t\t\t\t\t {self.pro2Var.get()} \n")

            if self.pro3Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductThree.get()} \t\t\t\t\t {self.pro3Var.get()} \n")

            if self.pro4Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductFour.get()} \t\t\t\t\t {self.pro4Var.get()} \n")

            if self.pro5Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductFive.get()} \t\t\t\t\t {self.pro5Var.get()} \n")

            if self.pro6Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductSix.get()} \t\t\t\t\t {self.pro6Var.get()} \n")

            if self.pro7Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductSeven.get()} \t\t\t\t\t {self.pro7Var.get()} \n")

            if self.pro8Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductEight.get()} \t\t\t\t\t {self.pro8Var.get()} \n")

            if self.pro9Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductNine.get()} \t\t\t\t\t {self.pro9Var.get()} \n")

            if self.pro10Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductTen.get()} \t\t\t\t\t {self.pro10Var.get()} \n")

            if self.pro11Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductEleven.get()} \t\t\t\t\t {self.pro11Var.get()} \n")

            if self.pro12Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductTwelve.get()} \t\t\t\t\t {self.pro12Var.get()} \n")

            if self.pro13Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductThirteen.get()} \t\t\t\t\t {self.pro13Var.get()} \n")

            if self.pro14Var.get() !=0:
               self.txtarea.insert(END,f" {self.ProductFourteen.get()} \t\t\t\t\t {self.pro14Var.get()} \n")


               self.txtarea.insert(END,"============================================================\n")
            if self.TotalVar.get() !=0 :   
               self.txtarea.insert(END,f"\t \t \t     Total: {self.TotalVar.get()} \n")
            if self.GSTVar.get() != 0 :  
               self.txtarea.insert(END,f"\t \t \t     GST: {self.GSTVar.get()} \n")
               
               self.txtarea.insert(END,"============================================================\n")
       
            if self.GrandTotalVar.get()!=0 :
               self.txtarea.insert(END,"============================================================\n")
               self.txtarea.insert(END,f"\t\t\t     Grand Total:{self.GrandTotalVar.get()} \n")
               self.txtarea.insert(END,"============================================================\n")
               self.save_bill()

    def save_bill(self):
        mes= messagebox.askyesno("Save","Do you want to save bill no." + self.BillNoVar.get()+ "?")
        if mes > 0:
            self.data = self.txtarea.get("1.0",END)
            file= open("F:/mini/bills/"+str(self.BillNoVar.get())+ ".txt", "w")
            file.write(self.data)
            file.close()
            messagebox.showinfo("Saved","Bill "+self.BillNoVar.get()+ " has saved successfully.")  
        else:
            return             
        
        #====================== Exit BUTTON Function ===========================================    
    def Window_Exit(self):
        mes= messagebox.askyesno("Notification","Do You want to close?")    
        if mes > 0:
            self.root.destroy()

root=Tk()
obj= Bill_Application(root)
root.mainloop()       