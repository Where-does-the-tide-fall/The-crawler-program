from tkinter import *


def callback():
    var.set('周末真的愉快么?')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('祝您周末愉快')
textLabel = Label(root, textvariable=var, justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='photo.gif')
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text='周末很愉快', command=callback)
theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
mainloop()
