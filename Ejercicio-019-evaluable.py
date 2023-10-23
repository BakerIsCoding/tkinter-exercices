from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.configure(background='Teal')
style = ttk.Style()
style.configure('TButton', background='red')
style.configure('TButton', font =('roboto', 14),borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'Navy Blue')],background = [('active', 'Navy Blue'), ('!disabled', 'black')], )

def showResponse(respuesta,type):
    messageType = ["askquestion","askokcancel","askyesno"]

    if respuesta:
        response.config(text="Has clicado 'Sí' en el bóton de " + messageType[type])
    else:
        response.config(text="Has clicado 'No' en el bóton de " + messageType[type])


def showAskQuestion():
    respuesta = messagebox.askquestion('Mensaje "askquestion"', '¿Quieres aceptar?')
    showResponse(respuesta,0)

def showAskOkCancel():
    respuesta = messagebox.askokcancel('Mensaje "askokcancel"', '¿Quieres aceptar?')
    showResponse(respuesta,1)

def showAskYesNo():
    respuesta = messagebox.askyesno('Mensaje "askyesno"', '¿Quieres aceptar?')
    showResponse(respuesta,2)

def showShowInfo():
    messagebox.showinfo('Mensaje "showinfo"', 'Este es un mensaje informativo')
    response.config(text="Mensaje informativo mostrado")

def showShowWarning():
    messagebox.showwarning('Mensaje "showwarning"', 'Este es un mensaje de advertencia')
    response.config(text="Mensaje de advertencia mostrado")

def showShowError():
    messagebox.showerror('Mensaje "showerror"', 'Este es un mensaje de error')
    response.config(text="Mensaje de error mostrado")


btnAskQuestion = ttk.Button(root, text="Mostrar mensaje 'askquestion'", command=showAskQuestion)
btnAskOkCancel = ttk.Button(root, text="Mostrar mensaje 'askokcancel'", command=showAskOkCancel)
btnAskYesNo = ttk.Button(root, text="Mostrar mensaje 'askyesno'", command=showAskYesNo)
btnShowInfo = ttk.Button(root, text="Mostrar mensaje 'showinfo'", command=showShowInfo)
btnShowWarning = ttk.Button(root, text="Mostrar mensaje 'showwarning'", command=showShowWarning)
btnShowError = ttk.Button(root, text="Mostrar mensaje 'showerror'", command=showShowError)

btnAskQuestion.grid(padx=15, pady=5)
btnAskOkCancel.grid(padx=15, pady=5)
btnAskYesNo.grid(padx=15, pady=5)
btnShowInfo.grid(padx=15, pady=5)
btnShowWarning.grid(padx=15, pady=5)
btnShowError.grid(padx=15, pady=5)

# Respuesta
response = tk.Label(root, text="De momento no has presionado ningún botón",font=36)
response.grid(pady=20)
response.configure(background='Teal')

root.mainloop()
