from tkinter import *
import requests

# creating the window
root = Tk()
root.title("Paypal")
root.geometry("500x500")
root.config(bg="yellow")

value = StringVar()
StringVar = IntVar()


information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
print(conversion_rate)


# Creating a label and entries


my_label1 = Label(root, text="Paypal Name", )
my_label1.place(x=5, y=10)

my_entry1 = Entry(root, width=10)
my_entry1.place(x=100, y=10)

my_label2 = Label(root, text="Email address",)
my_label2.place(x=5, y=40)

my_entry2 = Entry(root, width=10)
my_entry2.place(x=100, y=40)

my_label2 = Label(root, text="Choose currency")
my_label2.place(x=5, y=70)



# Doing the Conversion of the data with its loop


convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.place(x=130, y=90)


#def converting():
 #   num = float(my_entry1.get())
  #  print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
   # ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    #my_label3['text'] = ans


def clear():
    my_entry1.delete(0, END)


def exit_program():
    root.destroy()

# creating btn


convert_btn = Button(root, text="Submit", font=10, borderwidth="10", fg="black")
convert_btn.place(x=5, y=300)
clear_btn = Button(root, text="Clear", borderwidth="10", command=clear, fg="black")
clear_btn.place(x=300, y=300)
exit_btn = Button(root, text="Exit", borderwidth="10", command=exit_program, fg="black")
exit_btn.place(x=5, y=370)


root.mainloop()
