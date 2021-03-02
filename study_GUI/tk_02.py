import tkinter


class APP:
    def __init__(self, master):
        frame = tkinter.Frame(master)
        print(master)
        # 调整组件位置颜色之类的
        frame.pack(side=tkinter.LEFT, padx=10, pady=10)
        # 设置组件内的文字和颜色之类的
        self.hi_there = tkinter.Button(frame, text='打招呼',
                                       bg='black', fg='white',
                                       command=self.say_hello) # 调用say_hello方法
        # 调整位置
        self.hi_there.pack()

    def say_hello(self):
        print('你好!!')


# 创建窗口
root = tkinter.Tk()
app = APP(root)
print(app)
print(root)
# 视镜循环
root.mainloop()
