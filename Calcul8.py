from tkinter import *

root = Tk()
root.title("Calcul8")
root.option_add("*Font", "Consolas 20")


def add_to_input_text(next_val):
    current_text = input_text.get()
    input_text.set(current_text + next_val)


def answer():
    ans = eval(input_text.get())
    answer_value.set(ans)


def clear():
    input_text.set("")
    answer_value.set("")


input_text = StringVar()
input_text.set("")

answer_value = StringVar()
answer_value.set("")

button1 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=0, column=0, sticky=W+E)
button2 = Button(root, text="8", command=lambda: add_to_input_text("8")).grid(row=0, column=1, sticky=W+E)
button3 = Button(root, text="9", command=lambda: add_to_input_text("9")).grid(row=0, column=2, sticky=W+E)
button4 = Button(root, text="4", command=lambda: add_to_input_text("4")).grid(row=1, column=0, sticky=W+E)
button5 = Button(root, text="5", command=lambda: add_to_input_text("5")).grid(row=1, column=1, sticky=W+E)
button6 = Button(root, text="6", command=lambda: add_to_input_text("6")).grid(row=1, column=2, sticky=W+E)
button7 = Button(root, text="1", command=lambda: add_to_input_text("1")).grid(row=2, column=0, sticky=W+E)
button8 = Button(root, text="2", command=lambda: add_to_input_text("2")).grid(row=2, column=1, sticky=W+E)
button9 = Button(root, text="3", command=lambda: add_to_input_text("3")).grid(row=2, column=2, sticky=W+E)
button10 = Button(root, text="0", command=lambda: add_to_input_text("0")).grid(row=3, column=0, sticky=W+E)
button11 = Button(root, text="7", command=lambda: add_to_input_text("7")).grid(row=0, column=0, sticky=W+E)

button_add = Button(root, text="+", command=lambda: add_to_input_text("+")).grid(row=0, column=3, sticky=W+E)
button_sub = Button(root, text="-", command=lambda: add_to_input_text("-")).grid(row=1, column=3, sticky=W+E)
button_mul = Button(root, text="*", command=lambda: add_to_input_text("*")).grid(row=2, column=3, sticky=W+E)
button_div = Button(root, text="/", command=lambda: add_to_input_text("/")).grid(row=3, column=3, sticky=W+E)
button_ans = Button(root, text="=", command=lambda:answer()).grid(row=3, column=1, columnspan=2, sticky=W+E)

input_area = Label(root, textvariable=input_text, bg="hot pink", fg="white").grid(row=4, column=0, columnspan=4, sticky=W+E)
answer_area = Label(root, textvariable=answer_value, bg="blue", fg="white").grid(row=5, column=0, columnspan=4, sticky=W+E)

button_clear = Button(root, text="Clear", command=lambda: clear()).grid(row=6, column=0, columnspan=4, sticky=W+E)

root.mainloop()
