from tkinter import *
from PIL import Image, ImageTk

import random


class Pick:
    def __init__(self):
        self.root = root
        self.root.title("fr now")
        self.root.geometry("1200x600")
        self.root.config(bg="yellow")
        self.load = Image.open("lot.jpg")
        self.loader = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.loader)
        self.img.place(x=0, y=0)

        self.head_label = Label(text="Panda, Pusha , Play.", bg="yellow")
        self.head_label.place(x=270, y=10)

        # Your playing numbers
        self.output = Label(text="", width="30", height="2")
        self.output.place(x=380, y=140)
        self.output = Label(text="", width="30", height="2")
        self.output.place(x=380, y=185)
        self.output = Label(text="", width="30", height="2")
        self.output.place(x=380, y=230)
        self.number_label = Label(root, text="Your numbers")
        self.number_label.place(x=380, y=100)

        # Random numbers output
        self.output = Label(text="", width="30", height="2")
        self.output.place(x=680, y=140)
        self.number_label = Label(root, text="Draw", width="15")
        self.number_label.place(x=680, y=100)

        # Your numbers vs Draw output
        self.output = Label(text="", width="30", height="2")
        self.output.place(x=680, y=230)
        self.number_label = Label(root, text="Your numbers vs Draw")
        self.number_label.place(x=680, y=190)


# creating buttons
        self.btn1 = Button(text="1")
        self.btn1.place(x=10, y=100)
        self.btn2 = Button(text="2")
        self.btn2.place(x=50, y=100)
        self.btn3 = Button(text="3")
        self.btn3.place(x=90, y=100)
        self.btn4 = Button(text="4")
        self.btn4.place(x=130, y=100)
        self.btn5 = Button(text="5")
        self.btn5.place(x=170, y=100)
        self.btn6 = Button(text="6")
        self.btn6.place(x=210, y=100)

        self.btn7 = Button(text="7")
        self.btn7.place(x=10, y=140)
        self.btn8 = Button(text="8")
        self.btn8.place(x=50, y=140)
        self.btn9 = Button(text="9")
        self.btn9.place(x=90, y=140)
        self.btn10 = Button(text="10", width="1")
        self.btn10.place(x=130, y=140,)
        self.btn11 = Button(text="11", width="1")
        self.btn11.place(x=170, y=140,)
        self.btn12 = Button(text="12", width="1")
        self.btn12.place(x=210, y=140)

        self.btn13 = Button(text="13", width="1")
        self.btn13.place(x=10, y=180)
        self.btn14 = Button(text="14", width="1")
        self.btn14.place(x=50, y=180)
        self.btn15 = Button(text="15", width="1")
        self.btn15.place(x=90, y=180,)
        self.btn16 = Button(text="16", width="1")
        self.btn16.place(x=130, y=180,)
        self.btn17 = Button(text="17", width="1")
        self.btn17.place(x=170, y=180,)
        self.btn18 = Button(text="18", width="1")
        self.btn18.place(x=210, y=180)

        self.btn19 = Button(text="19", width="1")
        self.btn19.place(x=10, y=220)
        self.btn20 = Button(text="20", width="1")
        self.btn20.place(x=50, y=220)
        self.btn21 = Button(text="21", width="1")
        self.btn21.place(x=90, y=220,)
        self.btn22 = Button(text="22", width="1")
        self.btn22.place(x=130, y=220,)
        self.btn23 = Button(text="23", width="1")
        self.btn23.place(x=170, y=220,)
        self.btn24 = Button(text="24", width="1")
        self.btn24.place(x=210, y=220)

        self.btn25 = Button(text="25", width="1")
        self.btn25.place(x=10, y=260)
        self.btn26 = Button(text="26", width="1")
        self.btn26.place(x=50, y=260)
        self.btn27 = Button(text="27", width="1")
        self.btn27.place(x=90, y=260,)
        self.btn28 = Button(text="28", width="1")
        self.btn28.place(x=130, y=260,)
        self.btn29 = Button(text="29", width="1")
        self.btn29.place(x=170, y=260,)
        self.btn30 = Button(text="30", width="1")
        self.btn30.place(x=210, y=260)

        self.btn31 = Button(text="31", width="1")
        self.btn31.place(x=10, y=300)
        self.btn32 = Button(text="32", width="1")
        self.btn32.place(x=50, y=300)
        self.btn33 = Button(text="33", width="1")
        self.btn33.place(x=90, y=300,)
        self.btn34 = Button(text="34", width="1")
        self.btn34.place(x=130, y=300,)
        self.btn35 = Button(text="35", width="1")
        self.btn35.place(x=170, y=300,)
        self.btn36 = Button(text="36", width="1")
        self.btn36.place(x=210, y=300)

        self.btn37 = Button(text="37", width="1")
        self.btn37.place(x=10, y=340)
        self.btn38 = Button(text="38", width="1")
        self.btn38.place(x=50, y=340)
        self.btn39 = Button(text="39", width="1")
        self.btn39.place(x=90, y=340,)
        self.btn40 = Button(text="40", width="1")
        self.btn40.place(x=130, y=340,)
        self.btn41 = Button(text="41", width="1")
        self.btn41.place(x=170, y=340,)
        self.btn42 = Button(text="42", width="1")
        self.btn42.place(x=210, y=340)

        self.btn43 = Button(text="43", width="1")
        self.btn43.place(x=10, y=380)
        self.btn44 = Button(text="44", width="1")
        self.btn44.place(x=50, y=380)
        self.btn45 = Button(text="45", width="1")
        self.btn45.place(x=90, y=380,)
        self.btn46 = Button(text="46", width="1")
        self.btn46.place(x=130, y=380,)
        self.btn47 = Button(text="47", width="1")
        self.btn47.place(x=170, y=380,)
        self.btn48 = Button(text="48", width="1")
        self.btn48.place(x=210, y=380)
        self.btn49 = Button(text="49", width="1")
        self.btn49.place(x=10, y=420)

        self.btn12 = Button(text="Play", width="5", font="20", command=self.random())
        self.btn12.place(x=10, y=500)
        self.btn12 = Button(text="Clear", width="5", font="20")
        self.btn12.place(x=100, y=500)
        self.btn12 = Button(text="Exit", width="5", font="20")
        self.btn12.place(x=200, y=500)

    def random(self):
        self.randomlist = []
        for i in range(0, 6):
            self.n = random.randint(1, 49)
            self.randomlist.append(self.n)
            print(self.randomlist)


root = Tk()
app = Pick()
root.mainloop()
