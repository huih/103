# -*- coding: utf-8 -*-

from Tkinter import *
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("103")
        self.geometry("500x500+600+200")
        self.createMenu()
        self.createWidgets()

    def hello(self):
        print("xxx")

    def createMenu(self):
        self.menuBar = Menu(master = self)
        self.filemenu = Menu(self.menuBar, tearoff = 0)
        self.filemenu.add_command(label = "导出key", command = self.hello)
        self.filemenu.add_command(label = "设置问题", command = self.hello)
        self.filemenu.add_command(label = "关闭", command = self.quit)
        self.menuBar.add_cascade(label = "操作", menu = self.filemenu)

        self.helpmenu = Menu(self.menuBar, tearoff = 0)
        self.helpmenu.add_command(label = "支持", command = self.hello)
        self.helpmenu.add_command(label = "联系", command = self.hello)
        self.helpmenu.add_command(label = "关于", command = self.hello)
        self.menuBar.add_cascade(label = "帮助", menu = self.helpmenu)

        self.config(menu = self.menuBar)
        
    def createWidgets(self):
        pass
        

app = Application()
app.mainloop()
