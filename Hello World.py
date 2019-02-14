import tkinter
root = tkinter.Tk()

root.title('Hewwo wowd')  # sets the title of the window
root.geometry("600x200")  # sets the window's width and height

my_label = tkinter.Label(root)
my_label.config.text="Hewwo UwU", fg="#ff69b4" font=("windings")
my_label.grid()

root.mainloop()