# -*- coding: utf-8 -*-

import ttk
import time
import datetime
from Tkinter import *
from appintf.add_account import *
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("103")
        self.createMenu()
        self.geometry("800x200+200+200")
        data = self.load_data()
        self.createWidgets(data)
        self.createContextMenu()

    def load_data(self):
        result = []
        result.append({"name": "sohu", "url": "https://tv.sohu.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "baidu", "url": "https://www.baidu.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        result.append({"name": "sina", "url": "https://www.sina.com", "last_login_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return result

    def hello(self):
        print("xxx")

    def add_account(self):
        AddAccount(self)
    
    def user_event(self, event):
        item = self.tree.selection()[0]
        print ("you clicked on ", self.tree.item(item, "values"))

    def right_button_sel(self, event):
        self.context_menu.post(event.x_root,event.y_root)

    def createMenu(self):
        self.menuBar = Menu(master = self)
        self.filemenu = Menu(self.menuBar, tearoff = 0)
        self.filemenu.add_command(label = "增加账号", command = self.add_account)
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
        
    def createContextMenu(self):
        if self.tree is None:
            return

        #create right button menu
        self.context_menu = Menu(self.tree, tearoff = 0)
        self.context_menu.add_command(label = "删除", command = self.hello)        
        self.context_menu.add_command(label = "查看密码", command = self.hello)        
        
        
    def createWidgets(self, datas):
        self.tree = ttk.Treeview(master = self, show = "headings")
        vbar = ttk.Scrollbar(master = self, orient = VERTICAL, command = self.tree.yview)
        self.tree.configure(yscrollcommand = vbar.set)
        
        # name : current account identify name
        # url  : current redirection address 
        # type : current account type: application, html and so on
        self.tree["columns"]=("id", "name", "url", "last_login_time")  
        self.tree.column("id", width = 10)
        self.tree.column("name", width = 20) 
        self.tree.column("url", width = 100)  
        self.tree.column("last_login_time", width = 50)  
 
        self.tree.heading("id",  text="id") 
        self.tree.heading("name", text="别名")
        self.tree.heading("url", text="跳转地址")  
        self.tree.heading("last_login_time", text="上次登陆时间")
       
        index = 0 
        for d in datas:
            if index % 2 == 1:
                self.tree.insert("", index, values=(index, d["name"], d["url"], d["last_login_time"]), tags=('oddrow'))
            else:
                self.tree.insert("", index, values=(index, d["name"], d["url"], d["last_login_time"]), tags=('evenrow'))
            index += 1
        self.tree.tag_configure("oddrow", background = "#FDF5E6")
        self.tree.tag_configure("evenrow", background = "#f8f8f8")
        self.tree.pack(fill = BOTH)  
        self.tree.bind("<Double-1>", self.user_event)
        self.tree.bind("<Button-2>", self.right_button_sel)

app = Application()
app.mainloop()
