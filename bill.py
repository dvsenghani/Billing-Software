from tkinter import *
#from tkinter import font, colorchooser, filedialog, messagebox
import math, random, os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("Billing Software")

        bg_color="#074463"
        title = Label(self.root, text="DS Billing Software", bd=12, relief=GROOVE,bg=bg_color, fg='White',font=('times new roman',30,'bold'),pady=2).pack(fill=X)

        #--------------------------- Variables ------------------
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        self.rice = IntVar()
        self.flour = IntVar()
        self.food_oil = IntVar()
        self.vegatables = IntVar()
        self.chapati = IntVar()
        self.tea = IntVar()

        self.coca_cola = IntVar()
        self.Fanta = IntVar()
        self.Sprite = IntVar()
        self.Mdew = IntVar()
        self.Pepsi = IntVar()
        self.Limca = IntVar()

        #------------- Total Product Price & Tax Varibale ---------
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()


        # ------------ Customer Varibale ------------------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        #----------------------   Customer details frame  ------------------------
        
        F1 = LabelFrame(self.root,bd=10, relief=GROOVE, text="Customer Details", font=("times new roman",15,"bold"), fg="gold",bg=bg_color )
        F1.place(x=0, y=80, relwidth=1)

        # Customer label
        cname_lbl = Label(F1, text="Customer Name", bg = bg_color, fg='white' ,font=("times new roman",15,"bold")).grid(row=0, column=0,padx=20,pady=5)
        cname_entry = Entry(F1, width=20, textvariable=self.c_name, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg = bg_color, fg='white' ,font=("times new roman",15,"bold")).grid(row=0, column=2,padx=20,pady=5)
        cphn_entry = Entry(F1, width=15,textvariable = self.c_phone, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Bill Number", bg = bg_color, fg='white' ,font=("times new roman",15,"bold")).grid(row=0, column=4,padx=20,pady=5)
        cbill_entry = Entry(F1, width=15, textvariable = self.search_bill,font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)
        
        # Button
        bill_btn = Button(F1, text='Search', command=self.find_bill, width=10, bd=7, font='arial 12 bold').grid(row=0, column=6, pady=10, padx=10)

        #----------------------   Cosmetic Frame  ------------------------
     
        F2=LabelFrame(self.root,bd=10, relief=GROOVE, text="Cosmetic", font=("times new roman",15,"bold"), fg="gold",bg=bg_color )
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text='Bath Soap', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        bath_entry = Entry(F2, width=10, textvariable = self.soap,font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F2, text='Face Cream', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Face_cream_entry = Entry(F2, width=10,textvariable = self.face_cream, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Face_wash_lbl = Label(F2, text='Face Wash', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Face_wash_entry = Entry(F2, width=10,textvariable = self.face_wash, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_spray_lbl = Label(F2, text='Hair Spray', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Hair_spray_entry = Entry(F2, width=10, textvariable = self.spray, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_gel_lbl = Label(F2, text='Hair GEl', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Hair_gel_entry = Entry(F2, width=10,textvariable = self.gel, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_Lotion_lbl = Label(F2, text='Body Lotion', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Body_Lotion_entry = Entry(F2, width=10, textvariable = self.lotion, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #----------------------   Grocery Frame  ------------------------
     
        F3=LabelFrame(self.root,bd=10, relief=GROOVE, text="Grocery", font=("times new roman",15,"bold"), fg="gold",bg=bg_color )
        F3.place(x=340, y=180, width=325, height=380)

        bath_lbl = Label(F3, text='Rice', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        bath_entry = Entry(F3, width=10, textvariable = self.rice, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F3, text='Flour', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Face_cream_entry = Entry(F3, width=10, textvariable = self.flour, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Face_wash_lbl = Label(F3, text='Food oil', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Face_wash_entry = Entry(F3, width=10, textvariable = self.food_oil, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_spray_lbl = Label(F3, text='Vegetables', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Hair_spray_entry = Entry(F3, width=10,textvariable = self.vegatables, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_gel_lbl = Label(F3, text='Chapati', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Hair_gel_entry = Entry(F3, width=10, textvariable = self.chapati, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_Lotion_lbl = Label(F3, text='Tea', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Body_Lotion_entry = Entry(F3, width=10, textvariable = self.tea, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #----------------------   cold drinks Frame  ------------------------
     
        F4=LabelFrame(self.root,bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman",15,"bold"), fg="gold",bg=bg_color )
        F4.place(x=670, y=180, width=325, height=380)

        bath_lbl = Label(F4, text='Coca Cola', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        bath_entry = Entry(F4, width=10, textvariable = self.coca_cola, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F4, text='Fanta', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Face_cream_entry = Entry(F4, width=10,textvariable = self.Fanta, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Face_wash_lbl = Label(F4, text='Sprite', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Face_wash_entry = Entry(F4, width=10, textvariable = self.Sprite, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_spray_lbl = Label(F4, text='Mdew', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Hair_spray_entry = Entry(F4, width=10, textvariable = self.Mdew,font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_gel_lbl = Label(F4, text='Pepsi', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Hair_gel_entry = Entry(F4, width=10, textvariable = self.Pepsi, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_Lotion_lbl = Label(F4, text='Limca', font=('times new roman', 16,'bold'), bg=bg_color, fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Body_Lotion_entry = Entry(F4, width=10, textvariable = self.Limca, font=('times new roman', 16,'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #------------------- Bill Area ----------------
        
        F5=Frame(self.root,bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=280, height=380)
        
        bill_title=Label(F5, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5, orient=VERTICAL)
        self.txtarea=Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        

        #--------------- Button Frame -----------
        F6=LabelFrame(self.root,bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman",15,"bold"), fg="gold",bg=bg_color )
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1 = Label(F6, text='Total Cosmetic Price', font=('times new roman', 14,'bold'), bg=bg_color, fg='white').grid(row=0, column=0, padx=20, pady=1, sticky='w')
        m1_entry = Entry(F6, width=18, textvariable = self.cosmetic_price, font=('arial 10 bold'), bd=3, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)
        
        m2 = Label(F6, text='Total Grocery Price', font=('times new roman', 14,'bold'), bg=bg_color, fg='white').grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_entry = Entry(F6, width=18, textvariable = self.grocery_price, font=('arial 10 bold'), bd=3, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text='Total Cold Drinks Price', font=('times new roman', 14,'bold'), bg=bg_color, fg='white').grid(row=2, column=0, padx=20, pady=1, sticky='w')
        m3_entry = Entry(F6, width=18, textvariable = self.cold_drink_price, font=('arial 10 bold'), bd=3, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        
        #-------------- Tax -----------
        c1 = Label(F6, text='Cosmetic Tax', font=('times new roman', 14,'bold'), bg=bg_color, fg='white').grid(row=0, column=2, padx=20, pady=1, sticky='w')
        c1_entry = Entry(F6, width=18, textvariable = self.cosmetic_tax, font=('arial 10 bold'), bd=3, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)
        
        c2 = Label(F6, text='Grocery Tax', font=('times new roman', 14,'bold'), bg=bg_color, fg='white').grid(row=1, column=2, padx=20, pady=1, sticky='w')
        c2_entry = Entry(F6, width=18, textvariable = self.grocery_tax, font=('arial 10 bold'), bd=3, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text='Cold Drinks Tax', font=('times new roman', 14,'bold'), bg=bg_color, fg='white').grid(row=2, column=2, padx=20, pady=1, sticky='w')
        c3_entry = Entry(F6, width=18, textvariable = self.cold_drink_tax, font=('arial 10 bold'), bd=3, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=680, width=580, height=105)

        total_btn= Button(btn_F, comman=self.total, text='Total', bg='blue', fg='black', bd=2, pady=15, width=12, font='arial 14 bold').grid(row=0, column=0, padx=5, pady=5)
        GB_btn= Button(btn_F, text='Generate Bill',command=self.bill_area, bg='blue', fg='black', bd=2, pady=15, width=12, font='arial 14 bold').grid(row=0, column=1, padx=5, pady=5)
        Clear_btn= Button(btn_F, text='Clear',comman=self.clear_data, bg="blue", fg='black', bd=2, pady=15, width=12, font='arial 14 bold').grid(row=0, column=2, padx=5, pady=5)
        Exit_btn= Button(btn_F, text='Exit',command=self.Exit_app, bg='blue', fg='black', bd=2, pady=15, width=12, font='arial 14 bold').grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        self.cosmetic_soap = self.soap.get()*7.99
        self.cosmetic_face_cream = self.face_cream.get()*9.99
        self.cosmetic_face_wash = self.face_wash.get()*12.99
        self.cosmetic_spray = self.spray.get()*15.99
        self.cosmetic_gel = self.gel.get()*5.99
        self.cosmetic_lotion = self.lotion.get()*6.99

        self.total_cosmetic_price=float(
            self.cosmetic_soap +
            self.cosmetic_face_cream +
            self.cosmetic_face_wash +
            self.cosmetic_spray +
            self.cosmetic_gel +
            self.cosmetic_lotion
           
            )
        self.cosmetic_price.set("$ " + str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.07),2)
        self.cosmetic_tax.set("$ " + str(self.c_tax))
        


        self.grocery_rice = self.rice.get()*7.99
        self.grocery_food_oil = self.food_oil.get()*9.99
        self.grocery_vegatables = self.vegatables.get()*12.99
        self.grocery_tea = self.tea.get()*15.99
        self.grocery_flour = self.flour.get()*5.99
        self.grocery_chapati = self.chapati.get()*3.99

        self.total_grocery_price=float(
            self.grocery_rice +
            self.grocery_food_oil +
            self.grocery_vegatables +
            self.grocery_tea +
            self.grocery_flour +
            self.grocery_chapati

            )
        self.grocery_price.set("$ " + str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.03),2)
        self.grocery_tax.set("$ " + str(self.g_tax))



        self.drinks_coca_cola = self.coca_cola.get()*1.99
        self.drinks_Sprite = self.Sprite.get()*1.49
        self.drinks_Pepsi = self.Pepsi.get()*1.39
        self.drinks_Limca = self.Limca.get()*1.99
        self.drinks_Fanta = self.Fanta.get()*1.09
        self.drinks_Mdew = self.Mdew.get()*1.09

        self.total_drinks_price=float(
            self.drinks_coca_cola +
            self.drinks_Sprite +
            self.drinks_Pepsi +
            self.drinks_Limca +
            self.drinks_Fanta +
            self.drinks_Mdew 
            )
        self.cold_drink_price.set("$ " +str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price*0.07),2)
        self.cold_drink_tax.set("$ " + str(self.d_tax))

        
        #-----------total bill-------
        self.total_bill=float(self.total_cosmetic_price+
                        self.total_grocery_price+
                        self.total_drinks_price+
                        self.c_tax+
                        self.g_tax+
                        self.d_tax
                        )


    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t  DS Grocery Store\n\t2006 Fort Argyle rd")
        self.txtarea.insert(END, f"\n\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ===============================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n ===============================")



    def bill_area(self):
        if self.c_name.get()=='':
            messagebox.showerror("Error", 'Customer details are must')
        elif self.cosmetic_price.get()=="$ 0.0" and self.grocery_price.get()=="$ 0.0" and self.cold_drink_price.get()=="$ 0.0":
            messagebox.showerror("Error", 'No product purchased')

        else:
            self.welcome_bill()

        # ----- Cosmetic -------
            if self.soap.get()!=0:
                    self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t{self.cosmetic_soap}")
            if self.face_wash.get()!=0:
                    self.txtarea.insert(END, f"\n Face Lotion\t\t{self.face_cream.get()}\t{self.cosmetic_face_cream}")
            if self.face_cream.get()!=0:
                    self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t{self.cosmetic_face_wash}")
            if self.gel.get()!=0:
                    self.txtarea.insert(END, f"\n Hair Gel\t\t{self.gel.get()}\t{self.cosmetic_gel}")
            if self.spray.get()!=0:
                    self.txtarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t{self.cosmetic_spray}")
            if self.lotion.get()!=0:
                    self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t{self.cosmetic_lotion}")

    # ----- grocery -------
            if self.rice.get()!=0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t{self.grocery_rice}")
            if self.flour.get()!=0:
                self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t{self.grocery_flour}")
            if self.vegatables.get()!=0:
                self.txtarea.insert(END, f"\n Vegatables\t\t{self.vegatables.get()}\t{self.grocery_vegatables}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END, f"\n Food oil\t\t{self.food_oil.get()}\t{self.grocery_food_oil}")
            if self.chapati.get()!=0:
                self.txtarea.insert(END, f"\n Chapati\t\t{self.chapati.get()}\t{self.grocery_chapati}")
            if self.tea.get()!=0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t{self.grocery_tea}")

        # ----- Cold Drinks -------
            if self.coca_cola.get()!=0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.coca_cola.get()}\t{self.drinks_coca_cola}")
            if self.Sprite.get()!=0:
                self.txtarea.insert(END, f"\n Flour\t\t{self.Sprite.get()}\t{self.drinks_Sprite}")
            if self.Fanta.get()!=0:
                self.txtarea.insert(END, f"\n Vegatables\t\t{self.Fanta.get()}\t{self.drinks_Fanta}")
            if self.Mdew.get()!=0:
                self.txtarea.insert(END, f"\n Food oil\t\t{self.Mdew.get()}\t{self.drinks_Mdew}")
            if self.Limca.get()!=0:
                self.txtarea.insert(END, f"\n Chapati\t\t{self.Limca.get()}\t{self.drinks_Limca}")
            if self.Pepsi.get()!=0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.Pepsi.get()}\t{self.drinks_Pepsi}")


            self.txtarea.insert(END, f"\n -------------------------------")
        
            if self.cosmetic_tax.get()!='$ 0.0':
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!='$ 0.0':
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!='$ 0.0':
                self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            
        
            self.txtarea.insert(END, f"\n Total Bill:   \t\t $ {str(self.total_bill)}")
            self.txtarea.insert(END, f"\n -------------------------------")
            self.save_bill()


    def save_bill(self):
            op=messagebox.askyesno("Save Bill", "Do you want to save bill?")
            if op>0:
                self.bill_data=self.txtarea.get('1.0', END)
                f1=open("/Users/DS-MAC/Desktop/SSU/Python/Bill.py/bills/"+str(self.bill_no.get())+ ".txt", "w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill no: {self.bill_no} Saved")
            else:
                return

    def find_bill(self):
        present = 'no'
        for i in os.listdir('/Users/DS-MAC/Desktop/SSU/Python/Bill.py/bills/'):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"/Users/DS-MAC/Desktop/SSU/Python/Bill.py/bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present='yes'

        if present=='no':
            messagebox.showerror("Error", "No bill found")
        
    
    def clear_data(self):
        op=messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op>0:
            
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            self.rice.set(0)
            self.flour.set(0)
            self.food_oil.set(0)
            self.vegatables.set(0)
            self.chapati.set(0)
            self.tea.set(0)

            self.coca_cola.set(0)
            self.Fanta.set(0)
            self.Sprite.set(0)
            self.Mdew.set(0)
            self.Pepsi.set(0)
            self.Limca.set(0)

            #------------- Total Product Price & Tax Varibale ---------
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")


            # ------------ Customer Varibale ------------------
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")

            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit", "Do you really want to exit?")
        if op>0:
            self.root.destory()



root =Tk()
obj = Bill_App(root)
root.mainloop()