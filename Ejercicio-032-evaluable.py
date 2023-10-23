from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox

def strToInt(value):
    try:
        convertedValue = int(value)
        return convertedValue
    except Exception:
        return None

def strToFloat(value):
    try:
        convertedValue = float(value)
        return convertedValue
    except Exception:
        return None

def selectFromDb():
    #connect
    conection = sqlite3.connect("./databases/basquet.db")
    cursor = conection.cursor()
    #Select
    cursor.execute("SELECT *, oid FROM jugadors")

    resultados = cursor.fetchall()

    #print all
    for fila in resultados:
        print(fila)
    #close
    conection.close()


def reset():
    #Reset all Entrys
    nameEntry.delete(0, tk.END)
    surnameEntry.delete(0, tk.END)
    tallEntry.delete(0, tk.END)
    yOldEntry.delete(0, tk.END)

def connectDB():
    #Connect
    conection = sqlite3.connect("./databases/basquet.db")
    cursor = conection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadors (
        nom TEXT,
        cognom TEXT,
        alcada REAL,
        edat INTEGER
        )''')
    #Execute query
    conection.commit()
    #then close connection
    conection.close()



def send(name, surname, tall, years):
    finalTall = strToInt(years)
    finalYears = strToFloat(tall)

    #Check everything is good, to avoid errors
    if(name == "" or surname == "" or tall == "" or years == ""):
        messagebox.showerror('Error!"', 'No puedes dejar ningún campo vacío')
        return None
    if(finalYears == None):
        messagebox.showerror('Error!"', 'Error, Introduce un número entero o con decimales, en el campo Altura')
        return None

    if (finalTall == None):
        messagebox.showerror('Error!"', 'Error, Introduce un número entero, en el campo edad ')
        return None
    try:
        #Connect
        conection = sqlite3.connect("./databases/basquet.db")
        cursor = conection.cursor()
        #Get the parameters and then execute the query
        cursor.execute("INSERT INTO jugadors (nom, cognom, alcada, edat) VALUES (?, ?, ?, ?)",(name, surname, finalTall, finalYears))
        conection.commit()
        conection.close()
        #If everything goes well, display this message
        messagebox.showinfo('Datos almacenados correctamente"', 'Datos almacenados correctamente')
        #calling sellectFromDb(), prints the db information in the console
        selectFromDb()
        return True
    except Exception as e:
        messagebox.showerror('Error!', f'Ha ocurrido un error: {e}')
        return None



default = tk.Tk()
#Styles
style = ttk.Style()
style.configure('TButton', background='red')
style.configure('TButton', font =('roboto', 10),borderwidth = '4')
style.configure('Label.TLabel', font=('Arial', 12))
style.map('TButton', foreground = [('active', '!disabled', 'Navy Blue')],background = [('active', 'Navy Blue'), ('!disabled', 'black')], )

connectDB()
default.geometry("250x210")

titleLabel = tk.Label(default, text="Base De Datos", font=("Arial", 14, "bold")).place(x=50, y=5)

nameLabel = ttk.Label(default, text="Nombre:", style='Label.TLabel').place(x=10, y=40)
nameEntry = ttk.Entry(default)
surnameLabel = ttk.Label(default, text="Apellido:", style='Label.TLabel').place(x=10, y=70)
surnameEntry = ttk.Entry(default)
tallLabel = ttk.Label(default, text="Altura:", style='Label.TLabel').place(x=10, y=100)
tallEntry = ttk.Entry(default)
yOldLabel = ttk.Label(default, text="Edad:", style='Label.TLabel').place(x=10, y=130)
yOldEntry = ttk.Entry(default)

nameEntry.place(x=100, y=40)
surnameEntry.place(x=100, y=70)
tallEntry.place(x=100, y=100)
yOldEntry.place(x=100, y=130)


resetButton = ttk.Button(text="Reset Fields", command=reset)
sendButton = ttk.Button(text="Enviar", command=lambda:send(nameEntry.get(),surnameEntry.get(),tallEntry.get(),yOldEntry.get()))
sendButton.place(x=140, y=170)
resetButton.place(x=40, y=170)


default.mainloop()
