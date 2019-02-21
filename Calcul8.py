from tkinter import *

root = Tk()
root.title("Calcul8")


input_text = StringVar()
input_text.set("")

answer_value = StringVar()
answer_value.set("")

button1 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=0, column=0)
button2 = Button(root, text="8", command=lambda: add_to_input_text("8")).grid(row=0, column=1)
button3 = Button(root, text="9", command=lambda: add_to_input_text("9")).grid(row=0, column=2)
button4 = Button(root, text="5", command=lambda: add_to_input_text("5")).grid(row=1, column=0)
button5 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=1, column=1)
button6 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=1, column=2)
button7 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=2, column=0)
button8 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=2, column=1)
button9 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=2, column=2)
button10 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=0, column=0)
button11 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=0, column=0)


def add_to_input_text(next_val):
    current_text = input_text.get()
    input_text.set(curent_text*next_val)


root.mainloop()

