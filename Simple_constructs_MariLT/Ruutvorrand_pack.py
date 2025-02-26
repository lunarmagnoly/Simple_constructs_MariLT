from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


def Graafik():
    try:
        a = float(lbl_a.get())
        b = float(lbl_b.get())
        c = float(lbl_c.get())

        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        plt.figure()
        plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title("Quadratic Function Graph")
        plt.show()
    except ValueError:
        lbl_vastus.configure(text="Invalid input for graph")


def Lahenda():
    try:
        a = float(lbl_a.get())
        b = float(lbl_b.get())
        c = float(lbl_c.get())

        D = b**2 - 4 * a * c

        if D < 0:
            lbl_vastus.configure(text="No real solutions")
        elif D == 0:
            x = -b / (2 * a)
            lbl_vastus.configure(text=f"x = {x}")
        else:
            x1 = (-b + D**(1 / 2)) / (2 * a)
            x2 = (-b - D**(1 / 2)) / (2 * a)
            lbl_vastus.configure(text=f"x1 = {x1}, x2 = {x2}")
    except ValueError:
        lbl_vastus.configure(text="Invalid input! Enter numbers.")


def aken_grid():
    global lbl_a, lbl_b, lbl_c, lbl_vastus

    aken = Tk()  
    aken.geometry("650x400")
    aken.title("Quadratic Equation Solver")
    aken.resizable(False, False)

    f1 = Frame(aken, padx=20, pady=20)  
    f1.grid(row=0, column=0)

    lbl = Label(f1, text="Quadratic Equation Solver", font="Calibri 26", fg="green", bg="lightblue")
    lbl.grid(row=0, column=0, columnspan=6, pady=10)

    lbl_a = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=5)
    lbl_a.grid(row=1, column=0, padx=5)

    x2_label = Label(f1, text="x² +", font="Calibri 26", fg="green")
    x2_label.grid(row=1, column=1, padx=5)

    lbl_b = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=5)
    lbl_b.grid(row=1, column=2, padx=5)

    x_label = Label(f1, text="x +", font="Calibri 26", fg="green")
    x_label.grid(row=1, column=3, padx=5)

    lbl_c = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=5)
    lbl_c.grid(row=1, column=4, padx=5)

    equals_label = Label(f1, text="= 0", font="Calibri 26", fg="green")
    equals_label.grid(row=1, column=5, padx=5)

    btn_lahenda = Button(f1, text="Solve", font="Calibri 20", fg="white", bg="blue", command=Lahenda)
    btn_lahenda.grid(row=2, column=0, columnspan=3, pady=15, padx=10, ipadx=10)

    btn_graafik = Button(f1, text="Graph", font="Calibri 20", fg="white", bg="blue", command=Graafik)
    btn_graafik.grid(row=2, column=3, columnspan=3, pady=15, padx=10, ipadx=10)

    lbl_vastus = Label(f1, text="Solution will appear here", height=4, width=50, bg="yellow", font="Calibri 18")
    lbl_vastus.grid(row=3, column=0, columnspan=6, pady=20)

    aken.mainloop()


aken_grid()
