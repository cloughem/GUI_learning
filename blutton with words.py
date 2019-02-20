from tkinter import *

root = Tk()


def set_label1(text):
    labeltext.set(text)


labeltext = StringVar()
labeltext.set("")

button1 = Button(root)
button1.config(text="Hewwowdy pardner", bg="hot pink", command=lambda:set_label1("Hewwo"))
button1.grid()

button2 = Button(root)
button2.config(text="I'll do anything", bg="hot pink", command=lambda: set_label1("then perish"))
button2.grid()

label1 = Label(root)
label1.config(textvariable=labeltext)
label1.grid()

root.mainloop()
