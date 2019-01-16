from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text='Click me!')
button.pack()
ttk.Label(root, text='Hello, Tkinter!').pack()

root.mainloop()
