class MyStudent:
    def __init__(self, name, age, phone, favourite_colour):
        self.__name = name
        self.__age = age
        self.__phone_number = phone
        self.__favourite_color = favourite_colour
        self.__enrolled = True

    def get_name(self):
        """Getter function - returns the student's name"""
        return self.__name

    def get_age(self):
        """Getter function - returns the student's age"""
        return self.__age

    # age a student by one year
    def add_one_year(self):
        """Increments a student's age by 1 year."""
        print("Current age: ", self.__age)
        self.__age += 1
        print("New age: ", self.__age)

    def get_phone(self):
        """Getter function - returns the student's phone number"""
        return self.__phone_number

    def get_favecolour(self):
        """Getter function - returns the student's favourite colour"""
        return self.__favourite_color

    def get_enrolment_status(self):
        """Getter function - returns the student's enrolment status"""
        return self.__enrolled

    def enrol(self):
        """Sets a student's enrolment status to True."""
        self.__enrolled = True

    def unenrol(self):
        """Sets a student's enrolment status to False."""
        self.__enrolled = False

    # 3 checks, to ensure a valid value is being passed from the UI:
    # - is the name an empty string?
    # - is the name paramater None (common error if not passing correctly from UI)
    # - is new_name a string?
    def set_name(self, new_name):
        """Setter function - sets a new name for the student."""
        if new_name == "" or new_name is None or type(new_name) is not str:
            print("Name should be a string")
            return
        self.__name = new_name

    def set_age(self, new_age):
        """Setter function - sets a new age for the student."""
        # catches any invalid values being passed from the UI
        if new_age is None or type(new_age) is not int:
            print("Age must be an integer")
            return
            # simple boundary test - is the age positive?
        # for a student it might make sense to check "if not 13<=age<=18"
        if new_age <= 0:
            print("Age must be positive")
            return
        self.__age = new_age

    def set_phone(self, new_phone):
        self.__phone_number = new_phone

    # 3 checks, to ensure a valid value is being passed from the UI:
    # - is the colour an empty string?
    # - is the colour paramater None (common error if not passing correctly from UI)
    # - is colour a string?
    def set_favourite_colour(self, new_favourite_colour):
        """Setter function - sets a new favourite colour for the student."""
        if new_favourite_colour == "" or new_favourite_colour is None or type(new_favourite_colour) is not str:
            print("Colour must be a string")
            return
        self.__favourite_color = new_favourite_colour

    def print_details(self):
        """Prints a summary of the student's details to the console."""
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Phone:", self.__phone_number)
        print("Favourite colour:", self.__favourite_colour)

        if self.__enrolled:
            print("Enrolment status: enrolled.")
        else:
            print("Enrolment status: not enrolled.")


from tkinter import *

root = Tk()


def save_and_close(student, new_name, new_age, new_phone, new_colour, window, error):
    student.set_name(new_name)
    student.set_age(int(new_age))
    student.set_phone(new_phone)
    student.set_favourite_colour(new_colour))
    update_student_selector()
    close_window(window)


def close_window(window):
    window.destroy()


def get_student(fname):
    for student in student_list:      # for each student in the list
        if student.get_name() == fname:   # if they have the name we are looking for
            return student            # return that student object
    print("Student not found")        # debug message, will print to console


def update_details():
    student_name = student_selector.get(ACTIVE)
    current_student = get_student(student_name)
    str_name.set("Name: " + current_student.get_name())
    str_age.set("Age: " + str(current_student.get_age()))
    str_colour.set("Colour: " + current_student.get_favecolour())
    str_phone.set("Phone: " + current_student.get_phone())


def edit_student():
    edit_window = Toplevel(root)
    edit_window.title("Edit student details")
    edit_window.option_add("*Font", "LucidaGrande 20")

    Label(edit_window, text="Name:").grid(row=0, column=0, sticky=E)
    Label(edit_window, text="Age:").grid(row=1, column=0, sticky=E)
    Label(edit_window, text="Favourite colour:").grid(row=2, column=0, sticky=E)
    Label(edit_window, text="Phone number:").grid(row=3, column=0, sticky=E)

    student_name = student_selector.get(ACTIVE)
    current_student = get_student(student_name)

    str_current_name = StringVar(edit_window, current_student.get_name())
    str_current_age = StringVar(edit_window, str(current_student.get_age()))
    str_current_phone = StringVar(edit_window, current_student.get_phone())
    str_current_colour = StringVar(edit_window, current_student.get_favecolour())
    str_error_msg = StringVar("")

    entry_name = Entry(edit_window, textvariable=str_current_name).grid(row=0, column=1, sticky=E + W)
    entry_name = Entry(edit_window, textvariable=str_current_age).grid(row=1, column=1, sticky=E + W)
    entry_name = Entry(edit_window, textvariable=str_current_phone).grid(row=2, column=1, sticky=E + W)
    entry_name = Entry(edit_window, textvariable=str_current_colour).grid(row=3, column=1, sticky=E + W)

    Label(edit_window, textvariable=str_error_msg, fg="red").grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)

    Button(edit_window, text="Cancel", command=lambda: close_window(edit_window)).grid(row=5, column=0, sticky=E)
    Button(edit_window, text="Save",
           command=lambda: save_and_close(current_student, str_current_name.get(), str_current_age.get(),
                                          str_current_phone.get(), str_current_colour.get(), edit_window,
                                          str_error_msg)).grid(row=5, column=1, sticky=W)


root.title("Manage Your Students")
root.geometry("800x600")
root.option_add("*Font", "LucidaGrande 20")

# the button to update the details area
update_button = Button(root, text="Update details>>", command=lambda: update_details()).grid(row=10, column=0,
                                                                                             sticky=E + W)

str_name = StringVar(value="Full name: ")
str_age = StringVar(value="Age: ")
str_phone = StringVar(value="Phone: ")
str_colour = StringVar(value="Favourite colour: ")

# labels for all of the student details
full_name = Label(root, textvariable=str_name).grid(row=0, column=1, sticky=W)
age = Label(root, textvariable=str_age).grid(row=1, column=1, sticky=W)
phone_num = Label(root, textvariable=str_phone).grid(row=2, column=1, sticky=W)
fave_color = Label(root, textvariable=str_colour).grid(row=3, column=1, sticky=W)

student_list = []
student_list.append(MyStudent("Jacqui", 68, "0800dominos", "purple"))
student_list.append(MyStudent("Zara", 34, "1234", "red"))
student_list.append(MyStudent("Eliza", 18, "47325", "orange"))
student_list.append(MyStudent("Hanna", 17, "384278346891", "pink"))
student_list.append(MyStudent("Lina", 5, "5678", "black"))
student_list.append(MyStudent("Cate", 12, "999999999", "yellow"))

student_selector = Listbox(root, height=10)  # creates the listbox
for student in student_list:
    student_selector.insert(END, student.get_name())
student_selector.grid(row=0, column=0, rowspan=10)

edit_details = Button(root, text="Edit student details",
                      command=lambda: edit_student()).grid(row=4, column=1, sticky=E+W)


root.mainloop()
