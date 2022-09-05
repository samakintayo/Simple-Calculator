#BUILDING A SIMPLE CALCULATOR

from tkinter import *

root = Tk()
root.title("Tayo Simple Calculator")

#help(Entry)
e = Entry(root, width=40, borderwidth=7, bg= "green", font= "Calibri", fg= "white")
e.grid(row=0, column=0,columnspan=4, padx= 5, pady= 10)


#BUTTON CLICK FUNCTION DIPLAY THE DIGIT AND HOLDS IT FOR ANY FURTHER CALCULATION
def button_click(number):
    first_input = e.get()
    e.delete(0,END)
    e.insert(0,str(first_input)+str(number))
    return

#CLEAR FUNCTION
def clear():
    e.delete(0,END)


def add():
    first_input = float(e.get())
    e.delete(0, END)
    global action,var
    var= "add"
    action = first_input
    button_dot.config(state= ACTIVE)

#SUBTRACT FUNCTION CALL
def sub():
    first_input = float(e.get())
    e.delete(0, END)
    global action,var
    var= "sub"
    action = first_input
    button_dot.config(state= ACTIVE)

def mul():
    first_input = float(e.get())
    e.delete(0, END)
    global action, var
    var = "mul"
    action = first_input
    button_dot.config(state= ACTIVE)


def div():
    first_input = float(e.get())
    e.delete(0, END)
    global action, var
    var = "div"
    action = first_input
    button_dot.config(state= ACTIVE)

def dot():
    num = e.get()
    e.delete(0, END)
    e.insert(0, (num+ "."))
    if "." in str(e.get()):
        button_dot.config(state=DISABLED)

def extra():
    answer = e.get()
    e.delete(0,END)
    e.insert(0, answer )
    global action,var

    # button_add_dot.config(ACTIVE)

#EQUAL FUNTION
def equal():
    global action,var
    number= float(e.get())
    e.delete(0,END)
    if var == "add":
        e.insert(0,(action+number))

    if var == "sub":
        e.insert(0,(action-number))

    if var == "mul":
        e.insert(0,(action*number))

    if var == "div":
        e.insert(0,(action/number))

    if var == "dot":
        e.insert(0,(actionnumber))





#define button
button_1= Button(root, text= "1", padx=40, pady=20, command=lambda: button_click(1))
button_2= Button(root, text= "2", padx=40, pady=20, command=lambda: button_click(2))
button_3= Button(root, text= "3", padx=40, pady=20, command=lambda: button_click(3))
button_4= Button(root, text= "4", padx=40, pady=20, command=lambda: button_click(4))
button_5= Button(root, text= "5", padx=40, pady=20, command=lambda: button_click(5))
button_6= Button(root, text= "6", padx=40, pady=20, command=lambda: button_click(6))
button_7= Button(root, text= "7", padx=40, pady=20, command=lambda: button_click(7))
button_8= Button(root, text= "8", padx=40, pady=20, command=lambda: button_click(8))
button_9= Button(root, text= "9", padx=40, pady=20, command=lambda: button_click(9))

#arithmetic button
button_0= Button(root, text= "0", padx=40, pady=20, command=lambda: button_click(0))
button_add= Button(root, text= "+", padx=40, pady=20, command=add)
button_subtract= Button(root, text= "-", padx=40, pady=20, command=sub)
button_multiply= Button(root, text= "*", padx=40, pady=20, command=mul)
button_dot= Button(root, text= ".", padx=40, pady=20, command=dot)
button_divide= Button(root, text= "*", padx=40, pady=20, command=div)
button_extra= Button(root, text= "ANS", padx=80, pady=20, command=extra)
button_clear= Button(root, text= "Clr", padx=35, pady=20, command=clear)
button_equal= Button(root, text= "=", padx=40, pady=88, command= equal)

#button placing on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=1, column=3)
button_dot.grid(row=2, column=3)
button_divide.grid(row=3, column=3)
button_equal.grid(row=3, column=3
                  , rowspan=3)

button_extra.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2,)


#keeps the program running
root.mainloop()