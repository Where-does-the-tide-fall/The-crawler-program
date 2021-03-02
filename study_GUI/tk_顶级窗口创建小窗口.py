from tkinter import *

root = Tk()


def create():
    top = Toplevel()
    top.title('Pyton Demo')
    msg = Message(top)

Button(root, text='创建顶级窗口', command=create).pack()

mainloop()
