from tkinter import *

root = Tk()
root.geometry("500x400")

red_box = Label(root, text="red", bg="red", fg="white", height=20).grid(row=0, column=0, sticky=N+S)
green_box = Label(root, text="green", bg="green", fg="white", width=60, anchor=CENTER).grid(row=15, column=2, sticky=E+W)

root.mainloop()
