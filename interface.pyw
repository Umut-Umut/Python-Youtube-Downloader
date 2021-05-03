from tkinter import Label, Tk, Listbox, Entry, Button, PhotoImage
import asyncio as asy
import main

win = Tk()
win.geometry('1000x500')
win.title('ShammerTube')
win.configure(bg='green')

# ICON
icon = PhotoImage(file="images/icon.png")
win.iconphoto(False, icon)

# ENTRYS
ent1 = Entry(width=120)
ent2 = Entry(width=120)

# LABELS
lb1 = Label(bg='green')

# LISTBOX
lstbx1 = Listbox(width=120, height=22, bg='grey')

# BUTTONS
bt1 = Button(text='Start Order')
bt2 = Button(text='Download Video')
bt3 = Button(text='Download Audio')

# BUTTONS COMMAND
bt1.configure(command=lambda: main.startOrder(ent1.get(), lstbx1, lb1))
bt2.configure(command=lambda: main.download(lstbx1, ent2.get()))
bt3.configure(command=lambda: main.downloadAudio(ent1.get(), ent2.get(), lb1))

# LAYOUT
ent1.pack()
ent2.pack()

lstbx1.pack()

bt1.pack(side='left')
bt2.pack(side='right')
bt3.pack()

lb1.pack()

win.mainloop()
