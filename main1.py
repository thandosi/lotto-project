# Thandokazi Nkohla class 2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from playsound import playsound


class LottoForm:
    def __init__(self, ):
        self.root = root
        self.root.geometry("1000x750")
        self.root.title('Register')
        self.root.config(bg="yellow")
        self.load = Image.open("register.jpg")
        self.loader = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.loader)
        self.img.place(x=0, y=0)

        # My labels and entries
        self.name_label = Label(root, text="REGISTER", bg="green", width="10", borderwidth="12")
        self.name_label.place(x=10, y=10)

        self.name_label = Label(root, text="Enter your Name")
        self.name_label.place(x=10, y=90)
        self.name_entry = Entry()
        self.name_entry.place(x=150, y=90)

        self.surname_label = Label(root, text="Enter Surname")
        self.surname_label.place(x=10, y=120)
        self.surname_entry = Entry(root)
        self.surname_entry.place(x=150, y=120)

        self.email_label = Label(root, text="Enter your email: ")
        self.email_label.place(x=10, y=150)
        self.email_entry = Entry(root)
        self.email_entry.place(x=150, y=150)

        self.id_entry = Entry(root)
        self.id_entry.config(state='readonly')
        self.id_entry.place(x=150, y=180)

        self.email_validator = Button(root, text="Enter ID number: ", command=self.details, width=11)
        self.email_validator.place(x=10, y=180)

        self.login_btn = Button(root, text="login", command=self.id_verification, borderwidth="8", bg="Green")
        self.login_btn.place(x=10, y=250)



    def details(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = str(self.email_entry.get())

        if "@" in self.email_entry.get():
            self.id_entry.config(state='normal')

        else:
            messagebox.showinfo(title='Alert!', message="Please enter valid email Address!")
            self.id_entry.config(state='readonly')
            self.email_entry.delete(0, END)

    def id_verification(self):
        try:
            Id = int(self.id_entry.get())
            id_ls = self.id_entry.get()

            year = self.id_entry.get()[1]
            year2 = self.id_entry.get()[0:2]

            self.lotto_file = open('Lotto_file.txt', 'a+')
            self.lotto_file.write("Name: " + self.name_entry.get() + "| Player Email: " + self.email_entry.get() + "| Player ID: " + str(self.id_entry.get()) + "\n",)
            self.lotto_file.write("\n")
            self.lotto_file.close()

            if type(Id) == type(str()) or len(id_ls) != 13:
                raise ValueError
            elif int(year) <= 3:

                messagebox.showinfo(title="Let's Play!", message="Lets Play!")
                root.destroy()
            elif int(year2) > 3 and int(year2) > 21:
                messagebox.showinfo(title="Let's Play!", message="Lets Play!")
                root.destroy()
                import lott
            else:
                x = int(year) - 3
                messagebox.showinfo(title="Under Age", message="Your are too young to play")
        except ValueError:

            messagebox.showerror(title="Invalid Id", message="Please enter valid ID")
            self.id_entry.delete(0, END)


root = Tk()
lot = LottoForm()
root.mainloop()
