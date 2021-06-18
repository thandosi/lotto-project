from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

import random


class Pick:
    def __init__(self):
        self.root = root
        self.root.title("Lotto Machine")
        self.root.geometry("1200x600")
        self.root.config(bg="yellow")
        self.load = Image.open("lot.jpg")
        self.loader = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.loader)
        self.img.place(x=0, y=0)

        self.numbers = []
        self.numbers2 = []
        self.numbers3 = []
        self.numbers.sort()

        self.vs = []
        self.vs.sort()

        self.head_label = Label(text="Panda Pusha  Play.", bg="ROYAL BLUE")
        self.head_label.place(x=500, y=10)

        # Your playing numbers
        self.output1 = Entry(width="30")
        self.output1.place(x=300, y=140)
        self.output2 = Entry(width="30")
        self.output2.place(x=300, y=185)
        self.output3 = Entry(width="30")
        self.output3.place(x=300, y=230)
        self.number_label1 = Label(root, text="Your numbers", bg='ROYAL BLUE')
        self.number_label1.place(x=300, y=100)

        # Random numbers output
        self.output = Entry(width="30")
        self.output.place(x=580, y=140)
        self.number_label2 = Label(root, text="Draw", width="15", bg="royal blue")
        self.number_label2.place(x=580, y=100)

        # Your numbers vs Draw output
        self.output_vs = Entry(width="30")
        self.output_vs.place(x=880, y=140)
        self.output_vs = Entry(width="30")
        self.output_vs.place(x=880, y=180)
        self.output_vs = Entry(width="30")
        self.output_vs.place(x=880, y=220)

        self.number_label3 = Label(root, text="Your numbers vs Draw", bg="royal blue")
        self.number_label3.place(x=880, y=100)


# creating buttons
        self.btn1 = Button(text="1", command=lambda: self.insert('1'), bg="royal blue")
        self.btn1.place(x=10, y=100)
        self.btn2 = Button(text="2", command=lambda: self.insert('2'), bg="royal blue")
        self.btn2.place(x=50, y=100)
        self.btn3 = Button(text="3", command=lambda: self.insert('3'), bg="royal blue")
        self.btn3.place(x=90, y=100)
        self.btn4 = Button(text="4", command=lambda: self.insert('4'), bg="royal blue")
        self.btn4.place(x=130, y=100)
        self.btn5 = Button(text="5", command=lambda: self.insert('5'), bg="royal blue")
        self.btn5.place(x=170, y=100)
        self.btn6 = Button(text="6", command=lambda: self.insert('6'), bg="royal blue")
        self.btn6.place(x=210, y=100)

        self.btn7 = Button(text="7", command=lambda: self.insert(7), bg="royal blue")
        self.btn7.place(x=10, y=140)
        self.btn8 = Button(text="8", command=lambda: self.insert(8), bg="royal blue")
        self.btn8.place(x=50, y=140)
        self.btn9 = Button(text="9", command=lambda: self.insert(9), bg="royal blue")
        self.btn9.place(x=90, y=140)
        self.btn10 = Button(text="10", width="1", command=lambda: self.insert(10), bg="royal blue")
        self.btn10.place(x=130, y=140,)
        self.btn11 = Button(text="11", width="1", command=lambda: self.insert(11), bg="royal blue")
        self.btn11.place(x=170, y=140,)
        self.btn12 = Button(text="12", width="1", command=lambda: self.insert(12), bg="royal blue")
        self.btn12.place(x=210, y=140)

        self.btn13 = Button(text="13", width="1", command=lambda: self.insert(13), bg="royal blue")
        self.btn13.place(x=10, y=180)
        self.btn14 = Button(text="14", width="1", command=lambda: self.insert(14), bg="royal blue")
        self.btn14.place(x=50, y=180)
        self.btn15 = Button(text="15", width="1", command=lambda: self.insert(15), bg="royal blue")
        self.btn15.place(x=90, y=180,)
        self.btn16 = Button(text="16", width="1", command=lambda: self.insert(16), bg="royal blue")
        self.btn16.place(x=130, y=180,)
        self.btn17 = Button(text="17", width="1", command=lambda: self.insert(17), bg="royal blue")
        self.btn17.place(x=170, y=180,)
        self.btn18 = Button(text="18", width="1", command=lambda: self.insert(18), bg="royal blue")
        self.btn18.place(x=210, y=180)

        self.btn19 = Button(text="19", width="1", command=lambda: self.insert(19), bg="royal blue")
        self.btn19.place(x=10, y=220)
        self.btn20 = Button(text="20", width="1", command=lambda: self.insert(20), bg="royal blue")
        self.btn20.place(x=50, y=220)
        self.btn21 = Button(text="21", width="1", command=lambda: self.insert(21), bg="royal blue")
        self.btn21.place(x=90, y=220,)
        self.btn22 = Button(text="22", width="1", command=lambda: self.insert(22), bg="royal blue")
        self.btn22.place(x=130, y=220,)
        self.btn23 = Button(text="23", width="1", command=lambda: self.insert(23), bg="royal blue")
        self.btn23.place(x=170, y=220,)
        self.btn24 = Button(text="24", width="1", command=lambda: self.insert(24), bg="royal blue")
        self.btn24.place(x=210, y=220)

        self.btn25 = Button(text="25", width="1", command=lambda: self.insert(25), bg="royal blue")
        self.btn25.place(x=10, y=260)
        self.btn26 = Button(text="26", width="1", command=lambda: self.insert(26), bg="royal blue")
        self.btn26.place(x=50, y=260)
        self.btn27 = Button(text="27", width="1", command=lambda: self.insert(27), bg="royal blue")
        self.btn27.place(x=90, y=260,)
        self.btn28 = Button(text="28", width="1", command=lambda: self.insert(28), bg="royal blue")
        self.btn28.place(x=130, y=260,)
        self.btn29 = Button(text="29", width="1", command=lambda: self.insert(29), bg="royal blue")
        self.btn29.place(x=170, y=260,)
        self.btn30 = Button(text="30", width="1", command=lambda: self.insert(30), bg="royal blue")
        self.btn30.place(x=210, y=260)

        self.btn31 = Button(text="31", width="1", command=lambda: self.insert(31), bg="royal blue")
        self.btn31.place(x=10, y=300)
        self.btn32 = Button(text="32", width="1", command=lambda: self.insert(32), bg="royal blue")
        self.btn32.place(x=50, y=300)
        self.btn33 = Button(text="33", width="1", command=lambda: self.insert(33), bg="royal blue")
        self.btn33.place(x=90, y=300,)
        self.btn34 = Button(text="34", width="1", command=lambda: self.insert(34), bg="royal blue")
        self.btn34.place(x=130, y=300,)
        self.btn35 = Button(text="35", width="1", command=lambda: self.insert(35), bg="royal blue")
        self.btn35.place(x=170, y=300,)
        self.btn36 = Button(text="36", width="1", command=lambda: self.insert(36), bg="royal blue")
        self.btn36.place(x=210, y=300)

        self.btn37 = Button(text="37", width="1", command=lambda: self.insert(37), bg="royal blue")
        self.btn37.place(x=10, y=340)
        self.btn38 = Button(text="38", width="1", command=lambda: self.insert(38), bg="royal blue")
        self.btn38.place(x=50, y=340)
        self.btn39 = Button(text="39", width="1", command=lambda: self.insert(39), bg="royal blue")
        self.btn39.place(x=90, y=340,)
        self.btn40 = Button(text="40", width="1", command=lambda: self.insert(40), bg="royal blue")
        self.btn40.place(x=130, y=340,)
        self.btn41 = Button(text="41", width="1", command=lambda: self.insert(41), bg="royal blue")
        self.btn41.place(x=170, y=340,)
        self.btn42 = Button(text="42", width="1", command=lambda: self.insert(42), bg="royal blue")
        self.btn42.place(x=210, y=340)

        self.btn43 = Button(text="43", width="1", command=lambda: self.insert(43), bg="royal blue")
        self.btn43.place(x=10, y=380)
        self.btn44 = Button(text="44", width="1", command=lambda: self.insert(44), bg="royal blue")
        self.btn44.place(x=50, y=380)
        self.btn45 = Button(text="45", width="1", command=lambda: self.insert(45), bg="royal blue")
        self.btn45.place(x=90, y=380,)
        self.btn46 = Button(text="46", width="1", command=lambda: self.insert(46),bg="royal blue")
        self.btn46.place(x=130, y=380,)
        self.btn47 = Button(text="47", width="1", command=lambda: self.insert(47), bg="royal blue")
        self.btn47.place(x=170, y=380,)
        self.btn48 = Button(text="48", width="1", command=lambda: self.insert(48), bg="royal blue")
        self.btn48.place(x=210, y=380)
        self.btn49 = Button(text="49", width="1", command=lambda: self.insert(49), bg="royal blue")
        self.btn49.place(x=10, y=420)

        self.btn12 = Button(text="Play", width="5", font="20", command=self.random())
        self.btn12.place(x=10, y=500)
        self.btn12 = Button(text="Clear", width="5", font="20")
        self.btn12.place(x=100, y=500)
        self.btn12 = Button(text="Exit", width="5", font="20")
        self.btn12.place(x=200, y=500)

    def insert(self, val):
        self.output1.insert(END, val)
        self.output2.insert(END, val)
        self.output3.insert(END, val)

    def random(self):
        self.prizes = [0, 20, 100, 50, 2384, 8584, 10000000]
        self.matched = 0
        self.matched2 = 0
        self.matched3 = 0
        self.won = 0
        self. won2 = 0
        self.won3 = 0
        self.randomlist = random.sample(range(1, 49), 6)
        self.randomlist.sort()
        self.vs1 = set(self.numbers).intersection(set(self.randomlist))
        self.vs2 = set(self.numbers2).intersection(set(self.randomlist))
        self.vs3 = set(self.numbers3).intersection(set(self.randomlist))
        for number in self.numbers:
            if number in self.randomlist:
                self.matched += 1
            if self.matched == 2:
                self.won = self.prizes[2]
            elif self.matched == 3:
                self.won = self.prizes[3]
            elif self.matched == 4:
                self.won = self.prizes[4]
            elif self.matched == 5:
                self.won = self.prizes[5]
            elif self.matched == 6:
                self.won = self.prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(self.matched) + "\nEarnings: " + "R" + str(self.won) +
                                 "\nMatching number: " + str(self.vs1))

        for number in self.numbers2:
            if number in self.randomlist:
                self.matched2 += 1
            if self.matched2 == 2:
                self.won2 = self.prizes[2]
            elif self.matched2 == 3:
                self.won2 = self.prizes[3]
            elif self.matched2 == 4:
                self.won2 = self.prizes[4]
            elif self.matched2 == 5:
                self.won2 = self.prizes[5]
            elif self.matched2 == 6:
                self.won2 = self.prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(self.matched2) + "\nEarnings: " +
                                 "R" + str(self.won2) + "\nMatching number: " + str(self.vs2))

        for number in self.numbers3:
            if number in self.randomlist:
                self.matched3 += 1
            if self.matched3 == 2:
                self.won3 = self.prizes[2]
            elif self.matched3 == 3:
                self.won3 = self.prizes[3]
            elif self.matched3 == 4:
                self.won3 = self.prizes[4]
            elif self.matched3 == 5:
                self.won3 = self.prizes[5]
            elif self.matched3 == 6:
                self.won3 = self.prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(self.matched3) + "\nEarnings: " +
                                 "R" + str(self.won3) + "\nMatching number: " + str(self.vs3))

        if len(self.numbers) == 6 and len(self.numbers2) == 6 and len(self.numbers3) == 6:
            user_prize = float(self.won + self.won2 + self.won3)
            self.number_label1.config(text="R" + str(user_prize))
            self.number_label2.config(text="random-list")
        else:
            messagebox.showinfo("Error", "Please use all your tries first")
        for x in self.randomlist:
            if x in self.numbers:
                self.vs.append(x)
        self.output_vs.insert(0, self.vs)
        self.output.insert(0, self.randomlist)


root = Tk()
app = Pick()
root.mainloop()
