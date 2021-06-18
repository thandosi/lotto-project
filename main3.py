from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x300")
root.title("Payment")

class Method:
    def __init__(self, master):
        self.head_label = Label(master, text="Choose Payment Method")
        self.head_label.place(x=170, y=10)

        self.category_lbl = Label(master, text="Select Payment Method:")
        self.category_lbl.place(x=10, y=80)
        self.var = StringVar()
        self.category_list = ttk.Combobox(master, textvariable=self.var, width=12, value=["Bank Acc", "Paypal"])
        self.category_list.place(x=200, y=80)

        self.btn1 = Button(master, text="Next", command=self.choice())
        self.btn1.place(x=10, y=120)

    def choice(self):
        if self.category_list.get() == "Bank Acc":
            root.destroy()


app =Method(root)
root.mainloop()
