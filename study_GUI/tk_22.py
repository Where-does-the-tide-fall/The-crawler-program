from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'i love \n')
text.insert(END, 'python')


def show():
    print('你好呀')


b1 = Button(text, text='点我点我', command=show)
text.window_create(INSERT, window=b1)
mainloop()
