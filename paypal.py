from tkinter import *
import requests

# creating the window
root = Tk()
root.title("Paypal")
root.geometry("500x500")
root.config(bg="yellow")


class Paypal:
    def pay(self):

        self.value = StringVar()
        self.StringVar = IntVar()

        self.information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
        self.information_json = self.information.json()

        self.conversion_rate = self.information_json['conversion_rates']
        print(self.conversion_rate)


# Creating a label and entries
        self.my_label1 = Label(root, text="Paypal Name", )
        self.my_label1.place(x=5, y=10)

        self.my_entry1 = Entry(root, width=10)
        self.my_entry1.place(x=100, y=10)

        self.my_label2 = Label(root, text="Email address",)
        self.my_label2.place(x=5, y=40)

        self.my_entry2 = Entry(root, width=10)
        self.my_entry2.place(x=100, y=40)

        self.my_label2 = Label(root, text="Choose currency")
        self.my_label2.place(x=5, y=70)


# Doing the Conversion of the data with its loop
        self.convert_list = Listbox(root, width=20)
        for i in self.conversion_rate.keys():
            self.convert_list.insert(END, str(i))
        self.convert_list.place(x=130, y=90)


        #def converting():
         #   num = float(my_entry1.get())
          #  print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
           # ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
            #my_label3['text'] = ans


        def clear():
            self.my_entry1.delete(0, END)


        def exit_program():
            root.destroy()

# creating btn

        self.convert_btn = Button(root, text="Submit", font=10, borderwidth="10", fg="black")
        self.convert_btn.place(x=5, y=300)
        self.clear_btn = Button(root, text="Clear", borderwidth="10", command=clear, fg="black")
        self.clear_btn.place(x=300, y=300)
        self.exit_btn = Button(root, text="Exit", borderwidth="10", command=exit_program, fg="black")
        self.exit_btn.place(x=5, y=370)


root = Tk()
app = Paypal()
root.mainloop()
