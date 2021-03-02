from tkinter import *

root = Tk()

varlable = StringVar()
varlable.set('GO')

w = OptionMenu(root, varlable, 'one', 'two', 'three')
w.pack()

mainloop()
