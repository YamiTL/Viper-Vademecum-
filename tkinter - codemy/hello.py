from tkinter import Label
import tkinter as tk

# tk minuscula es el modulo, Tk es una clase
root = tk.Tk()
# Creating a Label widget
myLabel = Label(root, text="Hello World!")

# Show it on the screen
myLabel.pack()

root.mainloop()
