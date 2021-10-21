from form2tk.create import *
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import xlrd

nameList=[i for i in range(1,43)]
valueList=[i for i in range(1,43)]
def readdata(sfname):
    # 读取表格数据
    book = xlrd.open_workbook(sfname)
    sheet1 = book.sheets()[0]
    nrows = sheet1.nrows
    ##    print('表格总行数', nrows)
    ncols = sheet1.ncols
    ##    print('表格总列数', ncols)

    values = []
    for i in range(nrows):
        row_values = sheet1.row_values(i)
        values+=row_values
    return values,nrows,ncols

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("收支管理系统")
        self.root.geometry("600x400") 
        self.creat_res()
        self.root.mainloop()
    def creat_res(self):
        self.B1 = tk.Button(self.root, text="打开文件", command=self.openshow)
        self.B1.place(relx=0.03,rely=0.05)
        self.F1 = tk.Frame(self.root,bg='lightgrey')
        self.F1.place(relx=0.03,rely=0.15,relwidth=0.94,relheight=0.8)
        self.C1 = tk.Canvas(self.F1, bg='lightblue',width=300,height=300,scrollregion=(0,0,500,500))
        self.C1.place(relx=0,rely=0.0,relwidth=1,relheight=1)
        self.L1 = tk.Frame(self.C1)
##        self.L1.place(relx=0.53,rely=0.05,height=400)
        self.C1.create_window((20, 200),window=self.L1,anchor='w',width=500,height=380)
        self.L2 = tk.Label(self.root, text="单位:RMB")
        self.L2.place(relx=0.83,rely=0.05)
        scrollbar1=tk.Scrollbar(self.F1,orient="vertical",command=self.C1.yview)
##        scrollbar1.bind("<MouseWheel>", self.Wheel)
##        self.C1['yscrollcommand']=scrollbar1.set
        self.C1.config(yscrollcommand=scrollbar1.set)
##        scrollbar1.place(relx=0.93,rely=0.05,relheight=0.8)
        scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)


    def Wheel(self,event):#鼠标滚轮动作
        print(str(-1*(event.delta/120)))#windows系统需要除以120
##        self.F1.yview_scroll(int(-1*(event.delta/120)), "units")
##        text1.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def openshow(self):
        filename=self.openfile()
        data,maxr,maxc=readdata(filename)[0],readdata(filename)[1],readdata(filename)[2]
        a=biao(maxr,maxc)
        print(data)
        a.auto_Create_Text(self.L1,nameList,valueList)

        name=0
        for index,item in enumerate (data):
            '''↓↓↓向Label插入信息↓↓↓'''
            textList[name+1].configure(text=f'{data[name]}')
            temp=textList[name+1]
            temp.bind("<Button-1>",lambda event,arg=[name]:self.press(event,arg))
            temp.bind("<Button-3>",lambda event,arg=[name]:self.press_right(event,arg))
            temp.bind("<ButtonRelease-3>",self.out)
            name+=1
            '''↑↑↑向Label插入信息↑↑↑'''
    #选择文件
    def openfile(self):
        sfname = filedialog.askopenfilename(title='选择Excel文件', filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        return sfname
    def press(self,event,num):
        day=num[0]
        textList[num[0]+1].config(bg='lightgreen')
        pass
    def press_right(self,event,num):
        day=num[0]
        pop_x=event.x_root
        pop_y=event.y_root
        self.top=tk.Toplevel(bd=1,relief='solid')
        self.top.geometry("%dx%d+%d+%d" % (220, 180, pop_x, pop_y))
        self.top.overrideredirect(True)
        self.tempE=tk.Text(self.top,bg='lightblue')
        self.tempE.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.tempE.insert(0.0,f'当前选择{day}\n')
        self.tempE.insert(0.0,f'当前选择{day}\n')
        pass
    def out(self,*args):
        self.top.destroy()
        pass
if __name__=='__main__':
    ap=App()
