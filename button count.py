from tkinter import *

count = 0


def count_up():
    global count
    count += 1
    count_text.set(count)


def count_down():
    global count
    count -= 1
    count_text.set(count)


root = Tk()

count_text = StringVar()
count_text.set("0")

up_btn = Button(root)
up_btn.config(text="Count up", bg="black", fg="green", font="wingdings", command=count_up)
up_btn.grid()

down_btn = Button(root)
down_btn.config(text="Count down", bg="black", fg="pink", font="wingdings", command=count_down)
down_btn.grid()

count_label = Label(root)
count_label.config(textvariable=count_text)
count_label.grid()

root.mainloop()
