

        #-----------ALL IMAGES--------------
        self.search_b1=ImageTk.PhotoImage(file="F:/supplier1/button_images/search1.png")
        self.add_b1=ImageTk.PhotoImage(file="F:/supplier1/button_images/add2.png")
        self.update_b1=ImageTk.PhotoImage(file="F:/supplier1/button_images/update1.png")
        self.delete_b1=ImageTk.PhotoImage(file="F:/supplier1/button_images/remove.png")
        self.clear_b1=ImageTk.PhotoImage(file="F:/supplier1/button_images/clear2.png")
        self.show_b1=ImageTk.PhotoImage(file="F:/supplier1/button_images/show1.png")

        #----------MANAGE FRAME----------
    

    
        
        #----------BUTTON FRAME----------
        self.btn_frame=Frame(self.manage_frame,bd=5,relief=GROOVE,bg=bg_color)
        self.btn_frame.place(x=20,y=450,width=440)

        add_btn=Button(self.btn_frame,image=self.add_b1,width=85,height=35,bg=bg_color,bd=0,command=self.add_product).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(self.btn_frame,image=self.update_b1,width=85,height=35,bg=bg_color,bd=0,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(self.btn_frame,image=self.delete_b1,width=85,height=35,bg=bg_color,bd=0,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(self.btn_frame,image=self.clear_b1,width=85,height=35,bg=bg_color,bd=0,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        






        #----------DETAILS FRAME----------
        self.details_frame=Frame(self.root,bd=5,relief=RIDGE,bg=bg_color)
        self.details_frame.place(x=640,y=100,width=840,height=600)
        
        lbl_search=Label(self.details_frame,text="SEARCH BY",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(self.details_frame,textvariable=self.search_by,font=("times new roman",13),state='readonly',width=10)
        combo_search['values']=("product_name","product_id")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        self.txt_search=Entry(self.details_frame,width=15,textvariable=self.search_txt,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        search_btn=Button(self.details_frame,image=self.search_b1,text="SEARCH",width=90,height=30,bd=0,bg=bg_color,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(self.details_frame,image=self.show_b1,width=90,height=30,bg=bg_color,bd=0,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

       
