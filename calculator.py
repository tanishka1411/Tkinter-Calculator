from tkinter import *
import parser

root = Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')
root.geometry("300x300")

#configuring rows and columns so that it shrink and grow with your window
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
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N + E + W + S)

# Code to add buttons to the Calculator
Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0, sticky=N + S + E + W)
Button(root, text=" 2", command=lambda: get_variables(2)).grid(row=2, column=1, sticky=N + S + E + W)
Button(root, text=" 3", command=lambda: get_variables(3)).grid(row=2, column=2, sticky=N + S + E + W)

Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0, sticky=N + S + E + W)
Button(root, text=" 5", command=lambda: get_variables(5)).grid(row=3, column=1, sticky=N + S + E + W)
Button(root, text=" 6", command=lambda: get_variables(6)).grid(row=3, column=2, sticky=N + S + E + W)

Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0, sticky=N + S + E + W)
Button(root, text=" 8", command=lambda: get_variables(8)).grid(row=4, column=1, sticky=N + S + E + W)
Button(root, text=" 9", command=lambda: get_variables(9)).grid(row=4, column=2, sticky=N + S + E + W)

# adding other buttons to the calculator
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0, sticky=N + S + E + W)
Button(root, text=" 0", command=lambda: get_variables(0)).grid(row=5, column=1, sticky=N + S + E + W)
Button(root, text=" .", command=lambda: get_variables(".")).grid(row=5, column=2, sticky=N + S + E + W)

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=N + S + E + W)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=N + S + E + W)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=N + S + E + W)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=N + S + E + W)

# adding extra operations
Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4, sticky=N + S + E + W)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4, sticky=N + S + E + W)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=N + S + E + W)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4, sticky=N + S + E + W)
Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5, sticky=N + S + E + W)
Button(root, text="x!", command=lambda: fact()).grid(row=3, column=5, sticky=N + S + E + W)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=N + S + E + W)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N + S + E + W)
Button(root, text="=", command=lambda: calculate()).grid(columnspan=6, sticky=N + S + E + W)
root.mainloop()
