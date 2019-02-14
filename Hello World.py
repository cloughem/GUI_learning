import tkinter
root = tkinter.Tk()

root.title('Hewwo wowd')  # sets the title of the window
root.geometry("600x200")  # sets the window's width and height

my_label = tkinter.Label(root)
my_label.config(text="Hewwo UwU", fg="#ff69b4", bg="pink", font=("", "20"))
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Welcome to hell", fg="#ff69b4", bg="purple")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="You're trapped", fg="#ff69b4", bg="blue",  font=("Comic Sans ms", "50"), relief="ridge")
my_label.grid()

root.mainloop()