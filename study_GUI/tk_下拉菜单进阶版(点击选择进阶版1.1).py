from tkinter import *

OPTIONS=[
    'car',
    'cat',
    'hello',
    'love',
    'live',
    'like'
]
root = Tk()

varlable = StringVar()
varlable.set(OPTIONS[0])

w = OptionMenu(root, varlable, *OPTIONS)
w.pack()

mainloop()
