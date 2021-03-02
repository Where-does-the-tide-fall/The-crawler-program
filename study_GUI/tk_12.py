from tkinter import *

root = Tk()

Label(root, text='账号:').grid(row=0, column=0)
Label(root, text='密码:').grid(row=1, column=0)
v1 = StringVar()
v2 = StringVar()

# 输入框
e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show='*')
# 输入框放的位置
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print(f'账号:{e1.get()}')
    print(f'密码:{e2.get()}')


Button(root, text="芝麻开门", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
