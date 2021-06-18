from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.config(bg="yellow")
root.title("Lotto Machine")
root.geometry("1200x640")
load = Image.open("lot.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)


class LotteryNumbers:
    def __init__(self, master):
        self.numbers_label = Label(master, text="Good Luck", font="poppins 10", bg="yellow")
        self.numbers_label.place(x=300, y=10)

        self.btn1 = Button(master, text=1, command=lambda: self.on_click(1))
        self.btn1.place(x=10, y=100)
        self.btn2 = Button(master, text=2, command=lambda: self.on_click(2))
        self.btn2.place(x=50, y=100)
        self.btn3 = Button(master, text=3, command=lambda: self.on_click(3))
        self.btn3.place(x=90, y=100)
        self.btn4 = Button(master, text=4, command=lambda: self.on_click(4))
        self.btn4.place(x=130, y=100)
        self.btn5 = Button(master, text=5, command=lambda: self.on_click(5))
        self.btn5.place(x=170, y=100)
        self.btn6 = Button(master, text=6, command=lambda: self.on_click(6))
        self.btn6.place(x=210, y=100)

        self.btn7 = Button(master, text=7, command=lambda: self.on_click(7))
        self.btn7.place(x=10, y=140)
        self.btn8 = Button(master, text=8, command=lambda: self.on_click(8))
        self.btn8.place(x=50, y=140)
        self.btn9 = Button(master, text=9, command=lambda: self.on_click(9))
        self.btn9.place(x=90, y=140)
        self.btn10 = Button(master, text=10, command=lambda: self.on_click(10), width="1")
        self.btn10.place(x=130, y=140)
        self.btn11 = Button(master, text=11, command=lambda: self.on_click(11), width="1")
        self.btn11.place(x=170, y=140)
        self.btn12 = Button(master, text=12, command=lambda: self.on_click(12), width="1")
        self.btn12.place(x=210, y=140)

        self.btn13 = Button(master, text=13, command=lambda: self.on_click(13), width="1")
        self.btn13.place(x=10, y=180)
        self.btn14 = Button(master, text=14, command=lambda: self.on_click(14), width="1")
        self.btn14.place(x=50, y=180)
        self.btn15 = Button(master, text=15, command=lambda: self.on_click(15), width="1")
        self.btn15.place(x=90, y=180)
        self.btn16 = Button(master, text=16, command=lambda: self.on_click(16), width="1")
        self.btn16.place(x=130, y=180)
        self.btn17 = Button(master, text=17, command=lambda: self.on_click(17), width="1")
        self.btn17.place(x=170, y=180)
        self.btn18 = Button(master, text=18, command=lambda: self.on_click(18), width="1")
        self.btn18.place(x=210, y=180)

        self.btn19 = Button(master, text=19, command=lambda: self.on_click(19), width="1")
        self.btn19.place(x=10, y=220)
        self.btn20 = Button(master, text=20, command=lambda: self.on_click(20), width="1")
        self.btn20.place(x=50, y=220)
        self.btn21 = Button(master, text=21, command=lambda: self.on_click(21), width="1")
        self.btn21.place(x=90, y=220)
        self.btn22 = Button(master, text=22, command=lambda: self.on_click(22), width="1")
        self.btn22.place(x=130, y=220)
        self.btn23 = Button(master, text=23, command=lambda: self.on_click(23), width="1")
        self.btn23.place(x=170, y=220)
        self.btn24 = Button(master, text=24, command=lambda: self.on_click(24), width="1")
        self.btn24.place(x=210, y=220)

        self.btn25 = Button(master, text=25, command=lambda: self.on_click(25), width="1")
        self.btn25.place(x=10, y=260)
        self.btn26 = Button(master, text=26, command=lambda: self.on_click(26), width="1")
        self.btn26.place(x=50, y=260)
        self.btn27 = Button(master, text=27, command=lambda: self.on_click(27), width="1")
        self.btn27.place(x=90, y=260)
        self.btn28 = Button(master, text=28, command=lambda: self.on_click(28), width="1")
        self.btn28.place(x=130, y=260)
        self.btn29 = Button(master, text=29, command=lambda: self.on_click(29), width="1")
        self.btn29.place(x=170, y=260)
        self.btn30 = Button(master, text=30, command=lambda: self.on_click(30), width="1")
        self.btn30.place(x=210, y=260)

        self.btn31 = Button(master, text=31, command=lambda: self.on_click(31), width="1")
        self.btn31.place(x=10, y=300)
        self.btn32 = Button(master, text=32, command=lambda: self.on_click(32), width="1")
        self.btn32.place(x=50, y=300)
        self.btn33 = Button(master, text=33,command=lambda: self.on_click(33), width="1")
        self.btn33.place(x=90, y=300)
        self.btn34 = Button(master, text=34, command=lambda: self.on_click(34), width="1")
        self.btn34.place(x=130, y=300)
        self.btn35 = Button(master, text=35, command=lambda: self.on_click(35), width="1")
        self.btn35.place(x=170, y=300)
        self.btn36 = Button(master, text=36, command=lambda: self.on_click(36), width="1")
        self.btn36.place(x=210, y=300)

        self.btn37 = Button(master, text=37, command=lambda: self.on_click(37), width="1")
        self.btn37.place(x=10, y=340)
        self.btn38 = Button(master, text=38, command=lambda: self.on_click(38), width="1")
        self.btn38.place(x=50, y=340)
        self.btn39 = Button(master, text=39, command=lambda: self.on_click(39), width="1")
        self.btn39.place(x=90, y=340)
        self.btn40 = Button(master, text=40, command=lambda: self.on_click(40), width="1")
        self.btn40.place(x=130, y=340)
        self.btn41 = Button(master, text=41, command=lambda: self.on_click(41), width="1")
        self.btn41.place(x=170, y=340)
        self.btn42 = Button(master, text=42, command=lambda: self.on_click(42), width="1")
        self.btn42.place(x=210, y=340)

        self.btn43 = Button(master, text=43, command=lambda: self.on_click(43), width="1")
        self.btn43.place(x=10, y=380)
        self.btn44 = Button(master, text=44, command=lambda: self.on_click(44), width="1")
        self.btn44.place(x=50, y=380)
        self.btn45 = Button(master, text=45, command=lambda: self.on_click(45), width="1")
        self.btn45.place(x=90, y=380)
        self.btn46 = Button(master, text=46, command=lambda: self.on_click(46), width="1")
        self.btn46.place(x=130, y=380)
        self.btn47 = Button(master, text=47, command=lambda: self.on_click(47), width="1")
        self.btn47.place(x=170, y=380)
        self.btn48 = Button(master, text=48, command=lambda: self.on_click(48), width="1")
        self.btn48.place(x=210, y=380)
        self.btn49 = Button(master, text=49, command=lambda: self.on_click(49), width="1")
        self.btn49.place(x=10, y=420)

        self.your_numbers = Label(master, text="Your numbers", bg="royal blue")
        self.your_numbers.place(x=300, y=100)

        self.user_answers1 = Label(master, width=25)
        self.user_answers1.place(x=300, y=140)
        self.user_answers2 = Label(master, width=25)
        self.user_answers2.place(x=300, y=180)
        self.user_answers3 = Label(master, width=25)
        self.user_answers3.place(x=300, y=220)

        self.play_btn = Button(master, text="Play", command=self.play, bg="royal blue", borderwidth="10")
        self.play_btn.place(x=150, y=580)
        self.claim_btn = Button(master, text="Claim Price", bg="royal blue", borderwidth="10")
        self.claim_btn.place(x=250, y=580)
        self.replay_btn = Button(master, text="Play Again", command=self.play_again, bg="royal blue", borderwidth="10")
        self.replay_btn.place(x=400, y=580)
        self.prizes_label = Label(master, bg="royal blue")
        self.prizes_label.place(x=50, y=600)
        self.lotto_no = Label(master, bg="grey")
        self.lotto_no.place(x=50, y=550)
        self.number1 = []
        self.number2 = []
        self.number3 = []

    def on_click(self, pick):
        if len(self.number1) <= 5 and pick not in self.number1:
            self.number1.append(pick)
            self.user_answers1.config(text=self.number1)

        elif len(self.number1) == 6 and len(self.number2) <= 5 and pick not in self.number2:
            self.number2.append(pick)
            self.user_answers2.config(text=self.number2)

        elif len(self.number2) == 6 and len(self.number3) <= 5 and pick not in self.number3:
            self.number3.append(pick)
            self.user_answers3.config(text=self.number3)
        else:
            messagebox.showerror("Error", "You can only choose one number")

    def play(self):
        matched = 0
        matched2 = 0
        matched3 = 0
        winnings1 = 0
        winnings2 = 0
        winnings3 = 0
        prizes = [0, 0, 20, 100.50, 2384, 8584, 10000000]  # prizes in rands
        random_list = random.sample(range(1, 49), 6)
        random_list.sort()
        matching1 = set(self.number1).intersection(set(random_list))
        matching2 = set(self.number2).intersection(set(random_list))
        matching3 = set(self.number3).intersection(set(random_list))
        for number in self.number1:
            if number in random_list:
                matched += 1
            if matched == 2:
                winnings1 = prizes[2]
            elif matched == 3:
                winnings1 = prizes[3]
            elif matched == 4:
                winnings1 = prizes[4]
            elif matched == 5:
                winnings1 = prizes[5]
            elif matched == 6:
                winnings1 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(matched) + "\nwinnings: " + "R" + str(winnings1) +
                                 "\nMatching number: " + str(matching1))

        for number in self.number2:
            if number in random_list:
                matched2 += 1
            if matched2 == 2:
                winnings2 = prizes[2]
            elif matched2 == 3:
                winnings2 = prizes[3]
            elif matched2 == 4:
                winnings2 = prizes[4]
            elif matched2 == 5:
                winnings2 = prizes[5]
            elif matched2 == 6:
                winnings2 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(matched2) + "\nwinnings: " +
                                 "R" + str(winnings2) + "\nMatching number: " + str(matching2))

        for number in self.number3:
            if number in random_list:
                matched3 += 1
            if matched3 == 2:
                winnings3 = prizes[2]
            elif matched3 == 3:
                winnings3 = prizes[3]
            elif matched3 == 4:
                winnings3 = prizes[4]
            elif matched3 == 5:
                winnings3 = prizes[5]
            elif matched3 == 6:
                winnings3 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(matched3) + "\nwinnings: " +
                                 "R" + str(winnings3) + "\nMatching number: " + str(matching3))

        if len(self.number1) == 6 and len(self.number2) == 6 and len(self.number3) == 6:
            user_prize = float(winnings1 + winnings2 + winnings3)
            self.prizes_label.config(text="R" + str(user_prize))
            self.lotto_no.config(text=random_list)
        else:
            messagebox.showinfo("Error", "Please use all your tries first")

    def play_again(self):
        self.user_answers1.config(text="")
        self.user_answers2.config(text="")
        self.user_answers3.config(text="")
        self.prizes_label.config(text="")
        self.lotto_no.config(text="")
        self.number1 = []
        self.number2 = []
        self.number3 = []


numbers = LotteryNumbers(root)
root.mainloop()
