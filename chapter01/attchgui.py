from tkinter import *
from tkinter102 import MyGui


mainwin = Tk()
Label(mainwin, text=__name__).pack()


# 弹出窗口
popup = Toplevel()
Label(popup, text='attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
