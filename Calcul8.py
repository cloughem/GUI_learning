from tkinter import *

root = Tk()
root.title("Calcul8")


input_text = StringVar()
input_text.set("")

answer_value = StringVar()
answer_value.set("")


def add_to_input_text(next_val):
    current_text = input_text.get()
    input_text.set(curent_text*next_val)


root.mainloop()

