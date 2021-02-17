from tkinter import *
import parser
from math import factorial

i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

root = Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')
root.geometry("300x300")
Font_tuple = ("Helvetica", 13, "bold")

#configuring rows and columns so that they shrink and grow with window
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=2)
root.columnconfigure(4, weight=2)
root.columnconfigure(5, weight=2)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=2)
root.rowconfigure(4, weight=2)
root.rowconfigure(5, weight=2)
root.rowconfigure(6, weight=2)

# adding the input field
display = Entry(root, font=Font_tuple,justify="right",relief=RIDGE)
display.grid(row=1, columnspan=6, sticky=N + E + W + S,padx=3,pady=3)

# Code to add buttons to the Calculator
Button(root, text="1", command=lambda: get_variables(1), font=Font_tuple,relief=RIDGE).grid(row=2, column=0, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 2", command=lambda: get_variables(2), font=Font_tuple,relief=RIDGE).grid(row=2, column=1, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 3", command=lambda: get_variables(3), font=Font_tuple,relief=RIDGE).grid(row=2, column=2, sticky=N + S + E + W,padx=3,pady=3)

Button(root, text="4", command=lambda: get_variables(4), font=Font_tuple,relief=RIDGE).grid(row=3, column=0, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 5", command=lambda: get_variables(5), font=Font_tuple,relief=RIDGE).grid(row=3, column=1, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 6", command=lambda: get_variables(6), font=Font_tuple,relief=RIDGE).grid(row=3, column=2, sticky=N + S + E + W,padx=3,pady=3)

Button(root, text="7", command=lambda: get_variables(7), font=Font_tuple,relief=RIDGE).grid(row=4, column=0, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 8", command=lambda: get_variables(8), font=Font_tuple,relief=RIDGE).grid(row=4, column=1, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 9", command=lambda: get_variables(9), font=Font_tuple,relief=RIDGE).grid(row=4, column=2, sticky=N + S + E + W,padx=3,pady=3)

# adding other buttons to the calculator
Button(root, text="AC", command=lambda: clear_all(), font=Font_tuple,relief=RIDGE).grid(row=5, column=0, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" 0", command=lambda: get_variables(0), font=Font_tuple,relief=RIDGE).grid(row=5, column=1, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=" .", command=lambda: get_variables("."), font=Font_tuple,relief=RIDGE).grid(row=5, column=2, sticky=N + S + E + W,padx=3,pady=3)

Button(root, text="+", command=lambda: get_operation("+"), font=Font_tuple,relief=RIDGE).grid(row=2, column=3, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="-", command=lambda: get_operation("-"), font=Font_tuple,relief=RIDGE).grid(row=3, column=3, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="*", command=lambda: get_operation("*"), font=Font_tuple,relief=RIDGE).grid(row=4, column=3, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="/", command=lambda: get_operation("/"), font=Font_tuple,relief=RIDGE).grid(row=5, column=3, sticky=N + S + E + W,padx=3,pady=3)

# adding extra operations
Button(root, text="pi", command=lambda: get_operation("*3.14"), font=Font_tuple,relief=RIDGE).grid(row=2, column=4, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="%", command=lambda: get_operation("%"), font=Font_tuple,relief=RIDGE).grid(row=3, column=4, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="(", command=lambda: get_operation("("), font=Font_tuple,relief=RIDGE).grid(row=4, column=4, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="exp", command=lambda: get_operation("**"), font=Font_tuple,relief=RIDGE).grid(row=5, column=4, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="<-", command=lambda: undo(), font=Font_tuple,relief=RIDGE).grid(row=2, column=5, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="x!", command=lambda: fact(), font=Font_tuple,relief=RIDGE).grid(row=3, column=5, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text=")", command=lambda: get_operation(")"), font=Font_tuple,relief=RIDGE).grid(row=4, column=5, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="^2", command=lambda: get_operation("**2"), font=Font_tuple,relief=RIDGE).grid(row=5, column=5, sticky=N + S + E + W,padx=3,pady=3)
Button(root, text="=", command=lambda: calculate(), font=Font_tuple,relief=RIDGE).grid(columnspan=6, sticky=N + S + E + W,padx=3,pady=3)
root.mainloop()
