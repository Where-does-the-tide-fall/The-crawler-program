from tkinter import *

master = Tk()

thelB = Listbox(master, selectmode=EXTENDED, height=11)
thelB.pack()

# thelB.insert(0, '新年快乐')
# thelB.insert(END, '牛年大吉')
for item in range(11):
    thelB.insert(END, item)

# thelB.delete(0)

thelButton = Button(master, text='删除它', command=lambda x=thelB: x.delete(ACTIVE))
thelButton.pack()
mainloop()


