from tkinter import *

root = Tk()

w1 = Message(root, text='这是一则短消息', width=100)
w1.pack()
w2 = Message(root, text='这是一则\n超级巨无霸无敌长长长长长的消息', width=100)
w2.pack()


mainloop()
