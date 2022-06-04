from tkinter import *

alima = Tk()
alima.title("Halif calculator")


def click(number):
    #e1.delete(0, END)
    current = e1.get()
    e1.insert(0, str(current) + str(number))
def button_clear():
    e1.delete(0,END)
def button_add():
    x = e1.get()
    global f_num
    global math
    math = "addition"
    f_num = int(x)
    e1.delete(0, END)
def button_equal():
    y = e1.get()
    e1.delete(0, END)
    if math == "addition":
        e1.insert(0, f_num + int(y))
    if math == "subtraction":
        e1.insert(0, f_num - int(y))
    if math == "multiplication":
        e1.insert(0, f_num * int(y))
    if math == "division":
        e1.insert(0, f_num / int(y))

def b_multiply():
    x = e1.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(x)
    e1.delete(0, END)
def b_subtract():
    x = e1.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(x)
    e1.delete(0, END)

def b_divide():
    x = e1.get()
    global f_num
    global math
    math = "division"
    f_num = int(x)
    e1.delete(0, END)
e1 = Entry(alima, width=40, borderwidth=15, fg="violet", bg="black")
e1.grid(row=0, column=1, columnspan=3, padx=5, pady=10)
e3 = Button(alima, text="0", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(0)).grid(row=4, column=1)
e4 = Button(alima, text="1", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(1)).grid(row=1, column=1)
e5 = Button(alima, text="2", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(2)).grid(row=1, column=2)
e6 = Button(alima, text="3", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(3)).grid(row=1, column=3)
e7 = Button(alima, text="4", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(4)).grid(row=2, column=1)
e8 = Button(alima, text="5", padx=40, pady=20, fg="purple", bg="black",  command=lambda:click(5)).grid(row=2, column=2)
e9 = Button(alima, text="6", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(6)).grid(row=2, column=3)
e10 = Button(alima, text="7", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(7)).grid(row=3, column=1)
e11 = Button(alima, text="8", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(8)).grid(row=3, column=2)
e12 = Button(alima, text="9", padx=40, pady=20, fg="purple", bg="black", command=lambda:click(9)).grid(row=3, column=3)
e13 = Button(alima, text="+", padx=40, pady=20, fg="black", bg="violet", command=button_add).grid(row=1, column=4)
e14 = Button(alima, text="*", padx=40, pady=20, fg="black", bg="violet", command=b_multiply).grid(row=2, column=4)
e15 = Button(alima, text="-", padx=40, pady=20, fg="black", bg="violet", command=b_subtract).grid(row=3, column=4)
e16 = Button(alima, text="C", padx=40, pady=20, fg="black", bg="violet", command=button_clear).grid(row=4, column=4)
e17 = Button(alima, text="=", padx=40, pady=20, fg="black", bg="violet", command=button_equal).grid(row=4, column=2)
e18 = Button(alima, text="/", padx=40, pady=20, fg="black", bg="violet",command=b_divide).grid(row=4, column=3)


alima.mainloop()
