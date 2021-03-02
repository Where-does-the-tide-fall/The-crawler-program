from tkinter import *

# 生成root窗口
root = Tk()

# 窗口显示内容(Label可以显示图片)(调整内容位置和大小之类的)
textLabel = Label(root, text='祝您周末愉快', justify=LEFT,
                  padx=100)
# 自调整文字的位置
textLabel.pack(side=LEFT)
# 图片的名字及路径
photo = PhotoImage(file='photo.gif')
imageLabel = Label(root, image=photo)
# 调整图片的位置
imageLabel.pack(side=RIGHT)

mainloop()
