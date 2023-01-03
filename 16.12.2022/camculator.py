from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("eroare")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title("calculator")
    gui.geometry("470x250")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button1 = Button(gui, text=' 1 ', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    plus = Button(gui, text=' + ', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    button4 = Button(gui, text=' 4 ', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    minus = Button(gui, text=' - ', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    button7 = Button(gui, text=' 7 ', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    divide = Button(gui, text=' / ', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=4, column=3)

    button0 = Button(gui, text=' 0 ', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=1)

    multiply = Button(gui, text=' * ', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=5, column=3)

    power = Button(gui, text=' ^ ', command=lambda: press("^"), height=1, width=7)
    power.grid(row=6, column=3)

    dot = Button(gui, text=' . ', command=lambda: press("."), height=1, width=7)
    dot.grid(row=6, column=0)

    leftp = Button(gui, text=' ( ', command=lambda: press("("), height=1, width=7)
    leftp.grid(row=6, column=1)

    rightp = Button(gui, text=' ) ', command=lambda: press(")"), height=1, width=7)
    rightp.grid(row=6, column=2)

    clearbtn = Button(gui, text=' Clear ', command=lambda: clear(), height=1, width=7)
    clearbtn.grid(row=7, column=0)

    equal = Button(gui, text=' = ', command=lambda: equalpress(), height=1, width=7)
    equal.grid(row=7, column=3)

    gui.mainloop()