from tkinter import *

master = Tk()

thelB = Listbox(master, selectmode=EXTENDED)
thelB.pack()

# thelB.insert(0, '新年快乐')
# thelB.insert(END, '牛年大吉')
for item in ['鸡蛋', '鹅蛋', '鸭蛋', '狗蛋']:
    thelB.insert(END, item)

# thelB.delete(0)

thelButton = Button(master, text='删除它', command=lambda x=thelB: x.delete(ACTIVE))
thelButton.pack()
mainloop()

#
# class Fly(object):
#     def __init__(self, name='qwe', gender=1):
#         self.Name = name
#         self.Gender = gender
#         # return None
#         # return self.Gender
#
#
# f = Fly()
# print(f.Gender)
