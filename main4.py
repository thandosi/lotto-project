from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.config(bg="yellow")
root.title('Fill in Bank Details')

class Account:
    def __init__(self, master):
        self.head_label = Label(master, text="Fill in your details")
        self.head_label.place(x=170, y=10)
        self.head_label = Label(master, text="choose bank")
        self.head_label.place(x=10, y=90)
        self.head_label = Label(master, text="Account holder")
        self.head_label.place(x=10, y=120)
        self.head_label = Label(master, text="Account Number")
        self.head_label.place(x=10, y=150)
        self.head_label = Label(master, text="CVV")
        self.head_label.place(x=10, y=180)
        self.head_label = Label(master, text="Expiry Date")
        self.head_label.place(x=10, y=210)

        self.var = StringVar()
        self.category_list = ttk.Combobox(master, textvariable=self.var, width=12, value=["Capitec Bank", "FNB", "ABSA", "Standard Bank"])
        self.category_list.place(x=150, y=90)
        self.acc_entry = Entry()
        self.acc_entry.place(x=150, y=120)
        self.number_entry = Entry()
        self.number_entry.place(x=150, y=150)
        self.cvv_entry = Entry()
        self.cvv_entry.place(x=150, y=180)
        self.expiry_entry = Entry()
        self.expiry_entry.place(x=150, y=210)

        self.btn1 = Button(master, text="submit")
        self.btn1.place(x=10, y=250)

         



app =Account(root)
root.mainloop()
