from tkinter import *

"""翻牌子测试"""
root = Tk()
v = IntVar()
c = Checkbutton(root, text='测试一下', variable=v)
c.pack()

l = Label(root, textvariable=v)
l.pack()

mainloop()
