from tkinter import *
import requests
from PIL import Image, ImageTk

# creating the window
root = Tk()
root.title("Currency Converter")
root.geometry("700x450")
load = Image.open("payp.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)

value = StringVar()
StringVar = IntVar()


information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
print(conversion_rate)


# Creating a label and entries


my_label1 = Label(root, text="Your Earning", )
my_label1.place(x=5, y=10)
my_label2 = Label(root, text="Paypal Email", )
my_label2.place(x=5, y=40)


my_entry1 = Entry(root, textvariable=value, width=10)
my_entry1.place(x=100, y=10)
my_entry2 = Entry(root, textvariable=value, width=10)
my_entry2.place(x=100, y=40)

my_label3 = Label(root, text="Choose a Currency:")
my_label3.place(x=5, y=80)


# Doing the Conversion of the data with its loop


convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.place(x=100, y=120)


def converting():
    num = float(my_entry1.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    my_label3['text'] = ans


def clear():
    my_entry1.delete(0, END)


def exit_program():
    root.destroy()

# creating btn


convert_btn = Button(root, command=converting, text="Submit", font=10, bg="blue", borderwidth="10", fg="white")
convert_btn.place(x=5, y=320)
clear_btn = Button(root, text="Clear", borderwidth="10", bg="blue", command=clear, fg="white")
clear_btn.place(x=300, y=320)
exit_btn = Button(root, text="Exit", borderwidth="10", bg="blue", command=exit_program, fg="white")
exit_btn.place(x=5, y=390)


root.mainloop()
