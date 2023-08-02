from tkinter import *
win = Tk()

win.title("First Gui")        # title
win.iconbitmap('a.ico')  # icon

win.maxsize(width=600, height=300)  # size
win.minsize(width=600, height=300)  # size
# win.geometry("600x300")           # size for maxmize window

# Label
lbl = Label(win, text="User Name", bg="red", fg="white")
# lbl.pack()
# lbl.grid(row=3, colunm=3)
lbl.place(x=10, y=10)


# Entry
ent = Entry(win, bg="red", fg="white", width=10)
ent.place(x=80, y=10)


# Button


win.mainloop()  # last line of tkinter program


