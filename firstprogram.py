from tkinter import *

master = Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print(e.get())  # This is the text you may want to use later

b = Button(master, text="OK", width=10, command=callback)
b.pack()

mainloop()
