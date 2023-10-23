from tkinter import ttk
import tkinter as tk

buttonsColor = "#1E90FF"
windowColor = "#FFFFFF"
backgroundColor = "#E0E0E0"

window = tk.Tk()
window.title("Calculadora De Hector")
window.configure(background=backgroundColor)

resultDone = False

#Button Style
style = ttk.Style()
style.configure('TButton', font =('roboto', 20),borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],background = [('active', 'blue'), ('!disabled', 'black')], )


def buttonClicked(valor):
    global resultDone
    # If result pressed delete old numbers
    if (resultDone == True):
        resultDone = False
        if (valor == "/" or valor == "*" or valor == "+" or valor == "-"):
            print("Hi")
        else:
            entryText.delete(0, tk.END)
    # Delete text error
    if (entryText.get() == "Error"):
        entryText.delete(0, tk.END)

    # Apply entered button
    entryText.insert(1000, valor)


def erase():
    entryText.delete(0, tk.END)


def doMath():
    global resultDone
    try:
        textEntry = entryText.get()
        result = eval(textEntry)
        entryText.delete(0, tk.END)
        entryText.insert(0, result)
        resultDone = True
    except Exception as e:
        entryText.delete(0, tk.END)
        entryText.insert(0, "Error")


entryText = tk.Entry(window, font=("Roboto 20"), background=windowColor)
entryText.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

button0 = ttk.Button(window, text="0", width=4, command=lambda: buttonClicked(0), )
button1 = ttk.Button(window, text="1", width=4, command=lambda: buttonClicked(1))
button2 = ttk.Button(window, text="2", width=4, command=lambda: buttonClicked(2))
button3 = ttk.Button(window, text="3", width=4, command=lambda: buttonClicked(3))
button4 = ttk.Button(window, text="4", width=4, command=lambda: buttonClicked(4))
button5 = ttk.Button(window, text="5", width=4, command=lambda: buttonClicked(5))
button6 = ttk.Button(window, text="6", width=4, command=lambda: buttonClicked(6))
button7 = ttk.Button(window, text="7", width=4, command=lambda: buttonClicked(7))
button8 = ttk.Button(window, text="8", width=4, command=lambda: buttonClicked(8))
button9 = ttk.Button(window, text="9", width=4, command=lambda: buttonClicked(9))
buttonErase = ttk.Button(window, text="C", width=5, command=lambda: erase())
buttonSplit = ttk.Button(window, text="/", width=5, command=lambda: buttonClicked("/"))
buttonMultiply = ttk.Button(window, text="x", width=5, command=lambda: buttonClicked("*"))
buttonMinus = ttk.Button(window, text="-", width=5, command=lambda: buttonClicked("-"))
buttonSum = ttk.Button(window, text="+", width=5, command=lambda: buttonClicked("+"))
buttonEquals = ttk.Button(window, text="=", width=5, command=lambda: doMath())

# ROW 1
button7.grid(row=1, column=0, padx=2, pady=2)
button8.grid(row=1, column=1, padx=2, pady=2)
button9.grid(row=1, column=2, padx=2, pady=2)
buttonSplit.grid(row=1, column=3, padx=2, pady=2)

# ROW 2
button4.grid(row=2, column=0, padx=2, pady=2)
button5.grid(row=2, column=1, padx=2, pady=2)
button6.grid(row=2, column=2, padx=2, pady=2)
buttonMultiply.grid(row=2, column=3, padx=2, pady=2)

# ROW 3
button1.grid(row=3, column=0, padx=2, pady=2)
button2.grid(row=3, column=1, padx=2, pady=2)
button3.grid(row=3, column=2, padx=2, pady=2)
buttonMinus.grid(row=3, column=3, padx=2, pady=2)

# ROW 4
buttonErase.grid(row=4, column=0, padx=2, pady=2)
button0.grid(row=4, column=1, padx=2, pady=2)
buttonEquals.grid(row=4, column=2, padx=2, pady=2)
buttonSum.grid(row=4, column=3, padx=2, pady=2)

window.mainloop()
