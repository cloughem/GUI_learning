import tkinter

count = 0


def count_up():
    global count
    count += 1
    print(count)


def count_down():
    global count
    count -= 1
    print(count)


root = tkinter.Tk()

up_btn = tkinter.Button(root)
up_btn.config(text="Count up", bg="black", fg="green", command=count_up)
up_btn.grid()

down_btn = tkinter.Button(root)
down_btn.config(text="Count down", command=count_down)
down_btn.grid()

root.mainloop()
