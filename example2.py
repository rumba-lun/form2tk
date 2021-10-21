from form2tk.create import *
from tkinter import *
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("平铺演示")
        self.root.geometry("600x400") 
        self.creat_res()
        self.root.mainloop()
    def creat_res(self):
        self.F1 = tk.Frame(self.root,bg='lightgrey')    #用于绑定滚动条
        self.F1.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.C1 = tk.Canvas(self.F1, bg='lightblue',scrollregion=(0,0,700,550)) #默认位置和滚动比较
        self.T1 = tk.Text(self.C1,bg='lightblue',bd=0)
        self.T1.place(relx=0.02,rely=0.02,relwidth=0.3,relheight=0.1)
        self.T1.insert(tk.END, '这是一个平铺演示')
        
        self.L1 = tk.Frame(self.C1)     #表格父图层L1
        '''↓↓↓self.C1.create_window(a, b)中的a,b值可影响显示位置，需要调节'''
        self.C1.create_window((0, 600),window=self.L1,anchor='w',width=1920,height=1080)
        self.C1.place(relx=0,rely=0,relwidth=1,relheight=1)
##
        scrollbar1 = tk.Scrollbar(self.F1,orient="vertical",command=self.C1.yview)
        self.C1.config(yscrollcommand=scrollbar1.set)
        scrollbar1.pack(side=tk.RIGHT, fill=Y)
        scrollbar2 = tk.Scrollbar(self.F1,orient="horizontal",command=self.C1.xview)
        self.C1.config(xscrollcommand=scrollbar2.set)
        scrollbar2.pack(side=tk.BOTTOM, fill=X)
        self.draw_form()
    def draw_form(self):
        maxr=20     #你的表格行数
        maxc=20     #你的表格列数
        nameList=[i for i in range(1,maxr*maxc+1)]
        valueList=[i for i in range(1,maxr*maxc+1)]     #你的表格数据
        a=biao(maxr,maxc)
        a.auto_Create_Text(self.L1,nameList,valueList)

        name=0
        for i in range(maxr*maxc):
            '''↓↓↓向Label插入信息↓↓↓'''
            textList[name+1].insert(tk.END, f'{i+1}')
            textList[name+1].tag_add('center',1.0,'end')
            name+=1
if __name__=='__main__':
    ap=App()
