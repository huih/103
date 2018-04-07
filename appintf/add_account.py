# -*- coding: utf-8 -*-
import ttk
import time
import datetime
from Tkinter import *
class AddAccount(Tk):
    def __init__(self, parent):
        self.add_acc = Tk()
        self.add_acc.title("增加账号")
        self.add_acc.geometry("500x200+200+200")
        self.label_width = 10
        self.entry_width = 30
        self.padx = 50
        self.pady = 10

        #alias name
        Label(self.add_acc, text = "别名:", compound="right", width=self.label_width).grid(row = 0, column = 0, padx=self.padx, pady = self.pady) 
        name = StringVar()
        entry = Entry(self.add_acc, textvariable = name, width = self.entry_width)
        entry.grid(row = 0, column = 1)
        
        
        #account name
        Label(self.add_acc, text = "账号名:", compound="right", width=self.label_width).grid(row = 1, column = 0, pady=self.pady) 
        acc_name = StringVar()
        acc_entry = Entry(self.add_acc, textvariable = acc_name, width = self.entry_width)
        acc_entry.grid(row = 1, column = 1)

        #account password
        Label(self.add_acc, text = "密码:", compound="right", width=self.label_width).grid(row = 2, column = 0, pady=self.pady) 
        password = StringVar()
        pass_entry = Entry(self.add_acc, textvariable = password, width = self.entry_width)
        pass_entry.grid(row = 2, column = 1)

        #url
        Label(self.add_acc, text = "路径:", compound="right", width=self.label_width).grid(row = 3, column = 0, pady=self.pady) 
        url = StringVar()
        url_entry = Entry(self.add_acc, textvariable = url, width = self.entry_width)
        url_entry.grid(row = 3, column = 1)
        
        #button
        button = Button(self.add_acc, text="提交", command = self.add_account, width=10)
        button.grid(row = 4, column = 0, columnspan = 2)
        
        pass
    
    def add_account(self):
        print("xxx add account")
        pass

