from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import string
import os

# --------------------------- GLOBAL VARIABLES ----------------------------- #
encryption_key = 3
passcount = 0
themainpassword = ""
# ---------------------------- VIEW PASSWORD ------------------------------- #

# ------------------ WINDOW TO GET ALL PASSWORDS WITH MAIN PASSWORD CHECK -- #
def viewpass():
    newwin = Toplevel(window)
    newwin.title('Enter Main Password')
    newwin.geometry("400x100")

    # -------------- WINDOW WHICH SHOWS ALL PASSWORDS ----------------------- #
    def save1():

        Mainpassword = MainPassword.get()
        if Mainpassword == themainpassword:
            newwin2 = tk.Tk()
            newwin2.title("All Passwords")
            newwin2.geometry("1000x500")
            my_text = Text(newwin2, width=100, height=200, wrap='word')
            my_text.pack(pady=20)
            file = open('data.txt', 'r')
            f = file.readlines()
            newlist = []
            for line in f:
                if line[-1] == '\n':
                    newlist.append(line[:-1])
                else:
                    newlist.append(line)

            resultlist = [eval(x) for x in newlist]
            # print(newlist)
            for innerList in resultlist:
                passstring = innerList[2]
                innerList[2] = my_decrypt(passstring)
            resultstring = "Website\t\t\t\t\tUsername\t\t\t\t\tPassword\n"
            resultstring += "-"*200 + "\n"
            for innerList in resultlist:
                for innerItem in innerList:
                    resultstring += str(innerItem)+"\t\t\t\t\t"
                resultstring += "\n"
            my_text.config(state="normal")
            my_text.insert(tk.INSERT, resultstring)
            newwin.destroy()
        else:
            global passcount
            passcount += 1
            messagebox.showinfo(title="Password Checking",
                                message="Wrong Password")
            newwin.destroy()

    if passcount == 3:
        messagebox.showerror(title="Password rules violation",
                            message="Maximum attempts reached !!!")
        newwin.destroy()
        return
    EnterPass = Label(newwin, text=f"Enter the Main\n password: ({3-passcount} attempts remaining)")
    EnterPass.grid(row=1, column=0)
    MainPassword = Entry(newwin, width=25)
    MainPassword.focus()
    MainPassword.grid(row=1, column=2, columnspan=3)
    check_button = Button(newwin, text="Check Password",
                          width=20, command=save1)
    check_button.grid(row=2, column=1, columnspan=2, pady=5)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    alpha = string.ascii_letters
    digits = string.digits
    psw = ""
    for i in range(1, 7):
        if i % 2 == 0:
            psw = psw + random.choice(digits)
        else:
            psw = psw + random.choice(alpha)
    password_entry.delete(0, END)
    password_entry.insert(0, psw)


# --------------------------- ENCRYPT PASSWORD --------------------- #
def my_encrypt(s):
    l = list(s)
    res = []
    for x in l:
        res.append(chr(ord(x) + encryption_key))
    # print(res)
    return "".join(res)

# --------------------------- DECRYPT PASSWORD --------------------- #
def my_decrypt(s):
    l = list(s)
    res = []
    for x in l:
        res.append(chr(ord(x) - encryption_key))
    # print(res)
    return "".join(res)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f" \n Password: {password} \n is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"['{website}' , '{email}' , '{my_encrypt(password)}'] \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, " ")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2, pady=5)

# Buttons
generate_password_button = Button(
    text="Generate Password", width=16, command=generate)
generate_password_button.grid(row=4, column=2, pady=5)
add_button = Button(text="Add", width=16, command=save)
add_button.grid(row=4, column=1, pady=5)
view_password_button = Button(text="View Passwords", width=16, command=viewpass)
view_password_button.grid(row=6, column=1, pady=5)

# ---------------------------- SETTING ONE TIME PASSWORD ---------------------------#

def get_password():
    passfile = open("passfile.txt", 'w')
    passsetwin = Toplevel(window)
    passsetwin.title('Enter Main Password')
    passsetwin.geometry("400x100+600+300")
    EnterPass = Label(passsetwin, text=f"Set the Main Password:")
    EnterPass.grid(row=1, column=0)
    MainPassword = Entry(passsetwin, width=25)
    MainPassword.grid(row=2, column=0, padx="5")
    MainPassword.focus()

    def setPassword():
        global themainpassword
        main_pass = MainPassword.get()
        if main_pass == "":
            messagebox.showinfo("Problem","Please fill the one time password field !")
            get_password()
            passsetwin.destroy()
            return
        passfile.write(my_encrypt(main_pass))
        themainpassword = main_pass
        messagebox.showinfo("Success", "Password has been set successfully !")
        passsetwin.destroy()

    set_password_button = Button(passsetwin, text="Set Password",
                                 width=20, command=setPassword)
    set_password_button.grid(row=2, column=1, columnspan=2, pady=5)


# print(os.path.exists('passfile.txt'))
if os.path.exists('passfile.txt'):
    passfile = open("passfile.txt", 'r')
    line = passfile.readline()
    if line == '':
        get_password()
    else:
        themainpassword = my_decrypt(line)
else:
    get_password()


# -------------------------------- STARTING MAIN WINDOW ------------------ #
window.mainloop()
