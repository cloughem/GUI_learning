class Note:
    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_category(self):
        return self.__category


from tkinter import *


root = Tk()
root.title("Note Taker")
root.option_add("*font", "Consolas 20")
root.geometry("400x600")

notes = []


def save_note(window, title, body, category):
    new_note = Note(title.capitalize().strip(),
                    body.capitalize().strip(),
                    category.capitalize().strip())

    notes.append(new_note)
    print("Category: {}".format(new_note.get_category()))
    print("Title: {}".format(new_note.get_title()))
    print("Body: {}".format(new_note.get_text()))
    window.destroy()


def open_new_note(category):
    print("Open new note window")
    title_value = StringVar()
    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.grid()

    title_label = Label(new_note_window, text="Title:")
    title_label.grid(sticky=W)

    title_entry = Entry(new_note_window, textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note text:")
    note_label.grid(sticky=W)

    note_text = Text(new_note_window)
    note_text.config(height=10, width=20)
    note_text.grid()

    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="Cancel", command=new_note_window.destroy)
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame, text="Save",  command=lambda: save_note(new_note_window, title_value.get(),
                                                                               note_text.get(1.0, END), category))

    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_category):
    print("Open {}".format(list_category))
    list_window = Toplevel(root)
    list_window.geometry("600x400")

    for note in notes:
        title = note.get_title()
        body = note.get_text()
        category = note.get_category()

        note_text = "***{}***\n{}\n".format(title, body)

        if category == list_category:
            Label(list_window, text=note_text).grid(sticky=W)


lbl_title = Label(root, text="Notes")
lbl_title.config(font=("Calibri", "30"), width=20)
lbl_title.grid(row=0, sticky=N + E + S + W)

btn_shopping = Button(root, bg="#ffd9b3", fg="white",  text="Shopping", command=lambda: open_list("Shopping"))
btn_shopping.config()
btn_shopping.grid(row=1, sticky=E + W)

btn_shopping_new = Button(root, text="+", command=lambda: open_new_note("Shopping"))
btn_shopping_new.config()
btn_shopping_new.grid(column=1, row=1, sticky=E + W)

btn_todo = Button(root, bg="#ffffb3", fg="white",  text="To do", command=lambda: open_list("To do"))
btn_todo.config()
btn_todo.grid(row=2, sticky=E + W)

btn_homework = Button(root, bg="#d9ffb3", fg="white", text="Homework", command=lambda: open_list("Homework"))
btn_homework.config()
btn_homework.grid(row=3, sticky=E + W)

btn_but = Button(root, bg="#b3ffb3", fg="white", text="But", command=lambda: open_list("But"))
btn_but.config()
btn_but.grid(row=4, sticky=E + W)

btn_todo_new = Button(root, text="+", command=lambda: open_new_note("To do"))
btn_todo_new.config()
btn_todo_new.grid(column=1, row=2, sticky=E + W)

btn_homework_new = Button(root, text="+", command=lambda: open_new_note("Homework"))
btn_homework_new.config()
btn_homework_new.grid(column=1, row=3, sticky=E + W)

root.mainloop()