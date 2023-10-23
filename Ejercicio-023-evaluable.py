from tkinter import ttk
import tkinter as tk
import os
from tkinter import filedialog as quelcom
from tkinter import messagebox
from PIL import Image, ImageTk


def saveImage(originImage):
    try:
        saveRoute = quelcom.asksaveasfile(defaultextension=".jpg", filetypes=[("Archivos JPG", "*.jpg")])
        if saveRoute:
            originImage.save(saveRoute.name)
            messagebox.showinfo("Saved!", "El archivo se ha guardado correctamente")
    except OSError as error:
        messagebox.showerror("Error", str(error))



def fileManager():
    personalFiles = os.path.expanduser("~")
    file = quelcom.askopenfilename(initialdir=personalFiles+"//images//", filetypes = (("Imágenes", "*.jpg *.png"),))

    if(file):
        windowTop = tk.Toplevel()
        originImage = Image.open(file)
        tkImage = ImageTk.PhotoImage(originImage)

        imgLabel = tk.Label(windowTop, image=tkImage)
        imgLabel.image = tkImage
        imgLabel.pack()

        boton_guardar = ttk.Button(windowTop, text="Guardar imagen", command=lambda:saveImage(originImage))
        boton_guardar.pack()



default = tk.Tk()

style = ttk.Style()
style.configure('TButton', background='red')
style.configure('TButton', font =('roboto', 10),borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'Navy Blue')],background = [('active', 'Navy Blue'), ('!disabled', 'black')], )


tk.Label(text="Haz click en el siguiente botón para seleccionar una imagen:",font=("Arial", 18)).grid(padx=15, pady=15)
ttk.Button(text="Abrir archivo", command=fileManager).grid(padx=15, pady=15)

default.mainloop()
