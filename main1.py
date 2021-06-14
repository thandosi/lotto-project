# Thandokazi Nkohla class 2
import datetime
from tkinter import *


class LottoForm:
    def __init__(self, ):
        self.root = root
        self.root.geometry("600x600")
        self.root.title('For now')
        self.root.config(bg="yellow")


# creating my heading label
        self.my_heading = Label(root, text="Fill in your details", )
        self.my_heading.place(x=230, y=10)

# creating my labels

        self.name_label = Label(root, text="Name", bg="yellow")
        self.name_label.place(x=5, y=60)
        self.id_label = Label(root, text="ID number", bg="yellow")
        self.id_label.place(x=5, y=90)
        self.email_label = Label(root, text="Email", bg="yellow")
        self.email_label.place(x=5, y=120)

# creating the entries

        self.name_entry = Entry()
        self.name_entry.place(x=120, y=55)
        self.id_entry = Entry()
        self.id_entry.place(x=120, y=85)
        self.email_entry = Entry()
        self.email_entry.place(x=120, y=115)

        self.next_btn = Button(root, text="Let's Go")
        self.next_btn.place(x=5, y=180)
        self.clear_btn = Button(root, text="Clear", command=self.clear)
        self.clear_btn.place(x=120, y=180)

    def clear(self):
        self.name_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.email_entry.delete(0, END)

    def validate(self):
        date_time =datetime.datetime.now()



# creating buttons




root = Tk()
lot = LottoForm()
root.mainloop()
