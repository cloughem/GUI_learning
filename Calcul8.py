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
button4 = Button(root, text="4", command=lambda: add_to_input_text("4")).grid(row=1, column=0)
button5 = Button(root, text="5", command=lambda: add_to_input_text("5")).grid(row=1, column=1)
button6 = Button(root, text="6", command=lambda: add_to_input_text("6")).grid(row=1, column=2)
button7 = Button(root, text="1", command=lambda: add_to_input_text("1")).grid(row=2, column=0)
button8 = Button(root, text="2", command=lambda: add_to_input_text("2")).grid(row=2, column=1)
button9 = Button(root, text="3", command=lambda: add_to_input_text("3")).grid(row=2, column=2)
button10 = Button(root, text="0", command=lambda: add_to_input_text("0")).grid(row=3, column=0)
button11 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=0, column=0)

button_add = Button(root, text="+", command=lambda: add_to_input_text("+")).grid(row=0, column=3)
button_sub = Button(root, text="-", command=lambda: add_to_input_text("-")).grid(row=1, column=3)
button_X = Button(root, text="*", command=lambda: add_to_input_text("*")).grid(row=2, column=3)
button_div = Button(root, text="/", command=lambda: add_to_input_text("/")).grid(row=3, column=3)
button_ans = Button(root, text="=", command=lambda: add_to_input_text("=")).grid(row=0, column=0)

def add_to_input_text(next_val):
    current_text = input_text.get()
    input_text.set(curent_text*next_val)


root.mainloop()

