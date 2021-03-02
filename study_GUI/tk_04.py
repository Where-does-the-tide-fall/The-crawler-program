from tkinter import *

root = Tk()

photo = PhotoImage(file='photo3.gif')
theLabel = Label(root, text='学习Python\n 真是太开心了',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=('镇魂手书', 30,),
                 fg='black')
theLabel.pack()
mainloop()