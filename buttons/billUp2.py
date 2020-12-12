

        #============ ALL IMAGES ============#
        self.ttotal = ImageTk.PhotoImage(file="F:/supplier1/button_images/total1.png")
        self.Gen_bill=ImageTk.PhotoImage(file="F:/supplier1/button_images/genb.png")
        self.Clear_b=ImageTk.PhotoImage(file="F:/supplier1/button_images/clear.png")
        self.inventory_b=ImageTk.PhotoImage(file="F:/supplier1/button_images/inventory.png")
        self.exit_b=ImageTk.PhotoImage(file="F:/supplier1/button_images/exit.png")
        self.search_b=ImageTk.PhotoImage(file="F:/supplier1/button_images/search.png")
        self.add_b=ImageTk.PhotoImage(file="F:/supplier1/button_images/addc.png")
        self.f_b=ImageTk.PhotoImage(file="F:/supplier1/button_images/findb.png")
        #=============Variables==================#
       

        ##-------------Customer Detail Frame-------------##
        F1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,bg=bg_color,fg="white",text="Customer Name",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,textvariable=self.c_name,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,bg=bg_color,fg="white",text="Phone No.",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_lbl=Entry(F1,textvariable=self.c_phon,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,bg=bg_color,fg="white",text="Bill No.",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_lbl=Entry(F1,textvariable=self.search_bill,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,image=self.f_b,command=self.find_bill,width=113,bg=bg_color,text="Search",bd=0,font="arial 15 bold").grid(row=0,column=6,padx=20,pady=10)

        #============Search Items===============#


        #==============Button for search using item no.============
        search_no_btn=Button(F2,image=self.search_b,command=self.search_item,bg="Royalblue3",text="Search",fg="khaki",pady=10,width=120,bd=0,font="arial 15 bold").grid(row=1,column=1,padx=15,pady=5)
        
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



       

        #================Bottom Frame================#
     
        
        total_btn=Button(btn_F,image=self.ttotal,command=self.find_bill,bg="snow1",text="Total",fg="khaki",pady=12,width=162,bd=0,font="arial 15 bold")
        total_btn.grid(row=0,column=0,padx=12,pady=5)
       
        GBill_btn=Button(btn_F,image=self.Gen_bill,command=self.bill_area,bg="snow1",text="Generate Bill",fg="khaki",pady=12,width=169,bd=0,font="arial 15 bold").grid(row=0,column=1,padx=12,pady=5)
        Clear_btn=Button(btn_F,image=self.Clear_b,command=self.clear,bg="snow1",text="Clear",fg="khaki",pady=12,width=158,bd=0,font="arial 15 bold").grid(row=0,column=2,padx=12,pady=5)
        self.welcome_bill()


    

     

    