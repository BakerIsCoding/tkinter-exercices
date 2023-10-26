from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageTk

root = tk.Tk()
os.chdir("images")
root.iconbitmap("favicon.ico")
root.resizable(False,False)
root.configure(background='Teal')

imageList = ["random1.jpg","random2.jpg","random3.jpg","random4.jpg","random5.jpg"]
currentImg = 0

im = ImageTk.PhotoImage(Image.open(imageList[0]))
imgLabel = tk.Label(root, image=im)
imgLabel.grid(row=0, column=1, padx=5, pady=40)

#Button Style
style = ttk.Style()
style.configure('TButton', background='red')
style.configure('TButton', font =('roboto', 20),borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'Navy Blue')],background = [('active', 'Navy Blue'), ('!disabled', 'black')], )

def buttonClicked(choice):
    global imgLabel
    global currentImg
    if choice == "l":
        currentImg = currentImg-1
        if currentImg <= 0:
            currentImg = 0
            buttonNextLeft["state"]="disabled"  # disable left button
        buttonNextRight["state"]="normal"  # enable right button
        labelTotalImages.config(text="Imagen " + str(currentImg+1) + " de " + str(len(imageList)), font="arial") #reload image bottom right

    elif choice == "r":
        currentImg = currentImg+1
        if currentImg >= len(imageList)-1:
            currentImg = len(imageList)-1
            buttonNextRight["state"]="disabled"  # disable right button
        buttonNextLeft["state"]="normal"  # enable left button
        labelTotalImages.config(text="Imagen " + str(currentImg+1) + " de " + str(len(imageList)), font="arial") #reload image bottom right
    else:
        print("Error")

    newImg = ImageTk.PhotoImage(Image.open(imageList[currentImg]))
    imgLabel.configure(image=newImg)
    imgLabel.image = newImg

    imgLabel.grid(row=0, column=1, padx=5)


buttonNextLeft = ttk.Button(root, text="<", state="disabled", command=lambda:buttonClicked("l"),)
buttonNextLeft.grid(row=1, column=0, padx=30)
buttonNextLeft

buttonQuit = ttk.Button(root, text="Cerrar ventana", state="normal", command=lambda:root.quit())
buttonQuit.grid(row=1, column=1, padx=5)

buttonNextRight = ttk.Button(root, text=">", state="normal", command=lambda:buttonClicked("r"),)
buttonNextRight.grid(row=1, column=2, padx=30, pady=10)

labelTotalImages = tk.Label(root, text="Imagen " + str(currentImg+1) + " de " + str(len(imageList)), font="arial")
labelTotalImages.grid(row=2, column=2, padx=5)
labelTotalImages.configure(background='wheat', pady=5)


root.mainloop()

