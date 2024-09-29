from tkinter import Label, Button, Entry
import tkinter as tk

# tk minuscula es el modulo, Tk es una clase
root = tk.Tk()

campito = Entry(root, width=30)
campito.pack()
campito.insert(0, "Enter your name")


def myClick():
    hello = "Hello " + campito.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Send!", command=myClick, fg="pink", bg="black")
myButton.pack()


root.mainloop()
