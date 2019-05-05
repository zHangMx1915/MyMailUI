# _*_coding:utf-8 _*_
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from remail import get_msg



state = {'user': None, 'pass': None}
sums = 0
mail_content = ''


class Public:

    # 窗口居中显示
    def window_centered(self, window, width, height):
        sw = window.winfo_screenwidth()  # 得到屏幕宽度
        sh = window.winfo_screenheight()  # 得到屏幕高度
        x = (sw - (sw * width)) / 2
        y = (sh - (sh * height)) / 2
        width = sw * width
        height = sh * height
        swh = ("%dx%d+%d+%d" % (width, height, x, y))
        return swh

    # 退出当前界面的函数
    def loginusr_quit(self, window):
        window.destroy()


class LoginUi(Public):

    def __init__(self, window=None, var_usr_name=None, var_usr_pwd=None):
        self.window = window
        self.var_usr_name = var_usr_name
        self.var_usr_pwd = var_usr_pwd

    # 登录界面
    def set_login(self):
        self.window = tk.Tk()
        self.window.title("大鹅登陆页面")
        widths, heights = 0.3125, 0.37
        self.window.geometry(self.window_centered(self.window, widths, heights))
        self.window.resizable(0, 0)                           # 禁止调整窗口大小
        # self.window.iconbitmap("../MyPy/Photo/eee.ico")     # 应用图标

        canvas = tk.Canvas(self.window, height=180, width=600)
        image_file = tk.PhotoImage(file="Photo/beijingtu.png")
        canvas.create_image(0, 0, anchor='nw', image=image_file)
        canvas.pack(side='top')

        tk.Label(self.window, text='用户名:').place(x=190, y=200)
        tk.Label(self.window, text='密   码:').place(x=190, y=250)
        self.var_usr_name = tk.StringVar()
        # self.var_usr_name.set('请输入用户名')
        self.var_usr_pwd = tk.StringVar()
        # var_usr_pwd.set('请输入密码')
        entry_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name)
        entry_usr_name.focus()      # 默认光标
        entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, show='*')
        entry_usr_name.place(x=250, y=200)
        entry_usr_pwd.place(x=250, y=250)

        btn_login = tk.Button(self.window, text="登录", command=self.usr_login, width=19,
                              relief=RIDGE, activebackground='#0BB8A9', bd=2)
        btn_loguot = tk.Button(self.window, text="退出", command=self.usr_sign_quit, width=19,
                               relief=RIDGE, activebackground='#0BB8A9', bd=2)
        btn_login.place(x=240, y=300)
        btn_loguot.place(x=240, y=335)

        self.window.mainloop()

    # 写入ｊｓｏｎ
    def dump_json(self, usr_user):
        with open("date.json", "w") as f:
            json.dump(usr_user, f)

    # 关闭当前窗口，登录退出按钮专用
    def usr_sign_quit(self):
        global sums
        sums = 1
        self.window.destroy()

    # 校验登录
    def usr_login(self):
        global mail_content
        user_name, password = self.var_usr_name.get(), self.var_usr_pwd.get()      # 用户名及密码
        # 写入json
        usr_user = {}
        usr_user['user'] = user_name
        usr_user['pass'] = password
        str = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
        if re.match(str, user_name):
            self.dump_json(usr_user)

            # #　读取json
            # with open("../mymail/data_config.json") as fp:
            #     email_data = json.load(fp)
            # user = email_data['user']
            # password = email_data['pass']

            mail_content, user = get_msg(user_name, password)

            print(user, mail_content)

            self.loginusr_quit(self.window)
        else:
            # 弹出提示框
            str_var = tk.StringVar()
            str_var.set('askokcancel')
            messagebox.showwarning('提示信息', '错误！请检查用户名及密码！')
            str_var.set('askokcancel')


class MyMainPage(Public):

    def __init__(self):
        global mail_content
        self.window = tk.Tk()
        self.window.title("大鹅首页")
        widths, heights = 0.521, 0.648      # 1000, 700
        self.window.geometry(self.window_centered(self.window, widths, heights))
        # self.window.resizable(0, 0)  # 禁止调整窗口大小
        # self.window.iconbitmap("../MyPy/Photo/eee.ico")  # 应用图标

        tk.Label(self.window, text=mail_content, font='宋体 -14', pady=8).place(x=0, y=0)

        self.cai_dan(self.window)
        self.window.mainloop()

    # 菜单
    def cai_dan(self, top_var):
        menu = Menu(top_var)
        sub_menu_1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='查看', menu=sub_menu_1)
        sub_menu_2 = Menu(menu, tearoff=0)
        sub_menu_2.add_command(label='选项')
        sub_menu_2.add_command(label='颜色')
        menu.add_cascade(label='编辑', menu=sub_menu_2)
        sub_menu = Menu(menu, tearoff=0)
        sub_menu.add_command(label='查看帮助')
        sub_menu.add_separator()
        sub_menu.add_command(label='关于这只大鹅')
        menu.add_cascade(label='帮助', menu=sub_menu)
        top_var.config(menu=menu)


def main_go():
    a = LoginUi()
    a.set_login()
    if sums == 0:
        MyMainPage()


if __name__ == '__main__':
    main_go()
