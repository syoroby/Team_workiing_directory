from tkinter import *
import point            #point파일(두 점 사이의 거리 구하기) 임포트
from pandas import DataFrame
import matplotlib.pyplot as plt
import graph_function           # graph_function파일(지수 함수 그래프)임포트
import numpy as np


class btn_1(Toplevel):          #n차 함수 그래프
        def __init__(self):
                Toplevel.__init__(self)
                self.configure(background='white')
                self.geometry('300x450')

                self._frame = None
                self.switch_frame(StartPage)
                
        def switch_frame(self, frame_class):    
            new_frame = frame_class(self)
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack()

class StartPage(Frame):         #n차 함수 그래프 선택 화면
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='white')
        Label(self, text="함수를 선택하세요",
                              font = ("맑은 고딕", "21", 'bold'),
                              height=2,
                              foreground = '#087666',
                              background = 'white').pack(side="top", fill="x", pady=5)
        Button(self, text="1차함수",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=5)
        Button(self, text="2차함수",
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=5)
        Button(self, text="3차함수",
                  command=lambda: master.switch_frame(PageThree)).pack(pady=5)

class PageOne(Frame):           #1차 함수 그래프
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='white')
        Label(self, text="1 차 함 수",
                              font = ("맑은 고딕", "21", 'bold'),
                              foreground = '#087666',
                              background = 'white').pack(side="top", fill="x", pady=5)
        Label(self, text='y = ax + b',
                              font = ("맑은 고딕", "16", 'bold'),
                                foreground = '#31C9B3',
                                background = 'white').pack(fill='x')
        
        f1 = Frame(self, bg = 'white')
        f1.pack()        
       
        Label(f1, text='a =', background = 'white').grid(row = 0, column= 0, pady=5)
        Label(f1, text='b =', background = 'white').grid(row = 1, column = 0, pady=5)
        
        self.entryValue1 = StringVar()
        self.entry1 = Entry(f1, textvariable = self.entryValue1)

        self.entryValue2 = StringVar()
        self.entry2 = Entry(f1, textvariable = self.entryValue2)

        self.entry1.grid(row = 0, column = 1)
        self.entry2.grid(row = 1, column = 1)
        
        f2 = Frame(self, bg = '#b4dede')
        f2.pack()

        Label(f2, text='정의역의 범위', background = '#b4dede').grid(row = 0, column= 1, pady=3)
        
        Label(f2, text='최소', background = '#b4dede').grid(row = 1, column= 0, pady=5)
        Label(f2, text='최대', background = '#b4dede').grid(row = 2, column = 0, pady=5)
        
        self.entryValue3 = StringVar()
        self.entry3 = Entry(f2, textvariable = self.entryValue3)

        self.entryValue4 = StringVar()
        self.entry4 = Entry(f2, textvariable = self.entryValue4)

        self.entry3.grid(row = 1, column = 1)
        self.entry4.grid(row = 2, column = 1)

        btn = Button(self, text = "그래프 출력", command = self.draw_g1)
        btn.pack(pady=5)

        Button(self, text="이전화면으로 돌아가기",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=5)
                  
    def draw_g1(self):
        a = float(self.entryValue1.get())
        b = float(self.entryValue2.get())
        xmin = float(self.entryValue3.get())
        xmax = float(self.entryValue4.get())
        
        graph_function.graph1(a, b, xmin, xmax)   
    
class PageTwo(Frame):           #2차 함수 그래프
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='white')
        Label(self, text="2 차 함 수",
                              font = ("맑은 고딕", "21", 'bold'),
                              foreground = '#087666',
                              background = 'white').pack(side="top", fill="x", pady=5)
        Label(self, text='y = ax²+ bx + c',
                              font = ("맑은 고딕", "16", 'bold'),
                                foreground = '#31C9B3',
                                background = 'white').pack(fill='x')
        
        f1 = Frame(self, bg = 'white')
        f1.pack()        
       
        Label(f1, text='a =', background = 'white').grid(row = 0, column= 0, pady=5)
        Label(f1, text='b =', background = 'white').grid(row = 1, column = 0, pady=5)
        Label(f1, text='c =', background = 'white').grid(row = 2, column = 0, pady=5)
        
        self.entryValue1 = StringVar()
        self.entry1 = Entry(f1, textvariable = self.entryValue1)

        self.entryValue2 = StringVar()
        self.entry2 = Entry(f1, textvariable = self.entryValue2)
        
        self.entryValue3 = StringVar()
        self.entry3 = Entry(f1, textvariable = self.entryValue3)

        self.entry1.grid(row = 0, column = 1)
        self.entry2.grid(row = 1, column = 1)
        self.entry3.grid(row = 2, column = 1)
        
        f2 = Frame(self, bg = '#b4dede')
        f2.pack()

        Label(f2, text='정의역의 범위', background = '#b4dede').grid(row = 0, column= 1, pady=3)
        
        Label(f2, text='최소', background = '#b4dede').grid(row = 1, column= 0, pady=5)
        Label(f2, text='최대', background = '#b4dede').grid(row = 2, column = 0, pady=5)
        
        self.entryValue4 = StringVar()
        self.entry4 = Entry(f2, textvariable = self.entryValue4)

        self.entryValue5 = StringVar()
        self.entry5 = Entry(f2, textvariable = self.entryValue5)

        self.entry4.grid(row = 1, column = 1)
        self.entry5.grid(row = 2, column = 1)

        btn = Button(self, text = "그래프 출력", command = self.draw_g2)
        btn.pack(pady=5)
        
        Button(self, text="이전화면으로 돌아가기",
                  command=lambda: master.switch_frame(StartPage)).pack()
                  
    def draw_g2(self):
        a = float(self.entryValue1.get())
        b = float(self.entryValue2.get())
        c = float(self.entryValue3.get())
        xmin = float(self.entryValue4.get())
        xmax = float(self.entryValue5.get())
        
        graph_function.graph2(a, b, c, xmin, xmax)
                  
class PageThree(Frame):         #3차 함수 그래프
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='white')
        Label(self, text="3 차 함 수",
                              font = ("맑은 고딕", "21", 'bold'),
                              foreground = '#087666',
                              background = 'white').pack(side="top", fill="x", pady=5)
                              
        Label(self, text='y = ax³+ bx²+ cx + d',
                              font = ("맑은 고딕", "16", 'bold'),
                                foreground = '#31C9B3',
                                background = 'white').pack(fill='x')
        
        f1 = Frame(self, bg = 'white')
        f1.pack()        
       
        Label(f1, text='a =', background = 'white').grid(row = 0, column= 0, pady=5)
        Label(f1, text='b =', background = 'white').grid(row = 1, column = 0, pady=5)
        Label(f1, text='c =', background = 'white').grid(row = 2, column = 0, pady=5)
        Label(f1, text='d =', background = 'white').grid(row = 3, column = 0, pady=5)
        
        self.entryValue1 = StringVar()
        self.entry1 = Entry(f1, textvariable = self.entryValue1)

        self.entryValue2 = StringVar()
        self.entry2 = Entry(f1, textvariable = self.entryValue2)
        
        self.entryValue3 = StringVar()
        self.entry3 = Entry(f1, textvariable = self.entryValue3)
        
        self.entryValue4 = StringVar()
        self.entry4 = Entry(f1, textvariable = self.entryValue4)

        self.entry1.grid(row = 0, column = 1)
        self.entry2.grid(row = 1, column = 1)
        self.entry3.grid(row = 2, column = 1)
        self.entry4.grid(row = 3, column = 1)
        
        f2 = Frame(self, bg = '#b4dede')
        f2.pack()

        Label(f2, text='정의역의 범위', background = '#b4dede').grid(row = 0, column= 1, pady=3)
        
        Label(f2, text='최소', background = '#b4dede').grid(row = 1, column= 0, pady=5)
        Label(f2, text='최대', background = '#b4dede').grid(row = 2, column = 0, pady=5)
        
        self.entryValue5 = StringVar()
        self.entry5 = Entry(f2, textvariable = self.entryValue5)

        self.entryValue6 = StringVar()
        self.entry6 = Entry(f2, textvariable = self.entryValue6)

        self.entry5.grid(row = 1, column = 1)
        self.entry6.grid(row = 2, column = 1)

        btn = Button(self, text = "그래프 출력", command = self.draw_g3)
        btn.pack(pady=5)
        
        Button(self, text="이전화면으로 돌아가기",
                  command=lambda: master.switch_frame(StartPage)).pack()
                  
    def draw_g3(self):
        a = float(self.entryValue1.get())
        b = float(self.entryValue2.get())
        c = float(self.entryValue3.get())
        d = float(self.entryValue4.get())
        xmin = float(self.entryValue5.get())
        xmax = float(self.entryValue6.get())
        
        graph_function.graph3(a, b, c, d, xmin, xmax)                  

class btn_2(Toplevel):          #빗변의 길이
        def __init__(self):
                Toplevel.__init__(self)
                
                self.initialize()
                
        def initialize(self):
                self.configure(background='white')
                title = Label(self, text = '빗변의 길이',
                              font = ('맑은 고딕', '21', 'bold'),
                              height = 2,
                              foreground = '#087666',
                              background = 'white')
                title.pack()
                
                f1 = Frame(self, bg = 'white')
                f1.pack()
                
                txt1 = Label(f1, text = 'x값 입력: ',
                             background = 'white')
                txt2 = Label(f1, text = 'y값 입력: ',
                             background = 'white')

                txt1.grid(row = 0, column = 0)
                txt2.grid(row = 1, column = 0)

                self.entryValue1 = StringVar()
                self.entry1 = Entry(f1, textvariable = self.entryValue1)
                
                self.entryValue2 = StringVar()
                self.entry2 = Entry(f1, textvariable = self.entryValue2)
                
                self.entry1.grid(row = 0, column = 1)
                self.entry2.grid(row = 1, column = 1)
                
                btn = Button(self, text = '결과', command = self.Calculate)
                btn.pack()
                
                self.resultValue = StringVar()
                self.result = Label(self, bg = 'white',
                                    textvariable = self.resultValue)
                self.result.pack()
            
        def Calculate(self):
           a=float(self.entryValue1.get())
           b=float(self.entryValue2.get())
           c=(a*a)+(b*b) 
           
           result = "빗변의 길이는 => " + str(c) 
           self.resultValue.set(result)
           
class btn_3(Toplevel):          #지수 함수 그래프
        def __init__(self):
                Toplevel.__init__(self)
                
                self.initialize()
                
        def initialize(self):
                self.configure(background='white')
                title = Label(self, text = '지수 함수 그래프',
                              font = ('맑은 고딕', '21', 'bold'),
                              height = 2,
                              foreground = '#087666',
                              background = 'white')
                title.pack()
                
                f1 = Frame(self, bg = 'white')
                f1.pack()
                
                txt1 = Label(f1, text = 'x좌표의 최소값을 입력해주세요: ',
                             background = 'white')
                txt2 = Label(f1, text = 'x좌표의 최대값을 입력해주세요: ',
                             background = 'white')
                txt3 = Label(f1, text = '계수를 입력해주세요: ',
                             background = 'white')
                txt4 = Label(f1, text = '밑를 입력해주세요: ',
                             background = 'white')
                
                txt1.grid(row = 0, column = 0)
                txt2.grid(row = 1, column = 0)
                txt3.grid(row = 2, column = 0)
                txt4.grid(row = 3, column = 0)
                
                self.entryValue1 = StringVar()
                self.entry1 = Entry(f1, textvariable = self.entryValue1)
                
                self.entryValue2 = StringVar()
                self.entry2 = Entry(f1, textvariable = self.entryValue2)
                
                self.entryValue3 = StringVar()
                self.entry3 = Entry(f1, textvariable = self.entryValue3)
                
                self.entryValue4 = StringVar()
                self.entry4 = Entry(f1, textvariable = self.entryValue4)
                
                self.entry1.grid(row = 0, column = 1)
                self.entry2.grid(row = 1, column = 1)
                self.entry3.grid(row = 2, column = 1)
                self.entry4.grid(row = 3, column = 1)
                
                btn = Button(self, text = '그래프', command = self.draw)
                btn.pack()
                
                self.resultValue = StringVar()
                self.result = Label(self, bg = 'white',
                                    textvariable = self.resultValue)
                self.result.pack()
                
        def draw_graph(self, x, y):     # x, y축 추가
            plt.axvline(x=0, color = 'black')   
            plt.axhline(y=0, color = 'black')
    
            plt.plot(x, y)
            plt.grid(color='0.8')
            plt.show()
    
    
        def xrange(self, start, final, interval): # x값 범위 입력받아 저장
            numbers = [] 
            while start < final: 
                numbers.append(start) 
                start += interval 
            return numbers 


        def graph_log(self, front, under, xmin, xmax):
            x = self.xrange(xmin, xmax, 0.01) 
            y = []
            for t in x: 
                y.append(front*under**t) 
            self.draw_graph(x, y)
            
        def draw(self):
            xmin = float(self.entryValue1.get())
            xmax = float(self.entryValue2.get())
            front = float(self.entryValue3.get())
            under = float(self.entryValue4.get())
                
            self.graph_log(front,under,xmin,xmax)
            

class btn_4(Toplevel):
        def __init__(self):
                Toplevel.__init__(self)
                
                self.initialize()
                
        def initialize(self):
                self.configure(background='white')
                title = Label(self, text = '로그 함수 그래프',
                              font = ('맑은 고딕', '21', 'bold'),
                              height = 2,
                              foreground = '#087666',
                              background = 'white')
                title.pack()
                
                f1 = Frame(self, bg = 'white')
                f1.pack()
                
                txt1 = Label(f1, text = '함수: y = alog(x+b)+c',
                             background = 'white')
                txt2 = Label(f1, text = '로그의 밑을 입력해주세요: ',
                             background = 'white')
                txt3 = Label(f1, text = 'a를 입력해주세요: ',
                             background = 'white')
                txt4 = Label(f1, text = 'b를 입력해주세요: ',
                             background = 'white')
                txt5 = Label(f1, text = 'c를 입력해주세요: ',
                             background = 'white')
                txt6 = Label(f1, text = '정의역의 최소값을 입력해주세요: ',
                             background = 'white')
                txt7 = Label(f1, text = '정의역의 최대값을 입력해주세요: ',
                             background = 'white')
                
                txt1.grid(row = 0, column = 1)
                txt2.grid(row = 1, column = 0)
                txt3.grid(row = 2, column = 0)
                txt4.grid(row = 3, column = 0)
                txt5.grid(row = 4, column = 0)
                txt6.grid(row = 5, column = 0)
                txt7.grid(row = 6, column = 0)
                
                self.entryValue1 = StringVar()
                self.entry1 = Entry(f1, textvariable = self.entryValue1)
                
                self.entryValue2 = StringVar()
                self.entry2 = Entry(f1, textvariable = self.entryValue2)
                
                self.entryValue3 = StringVar()
                self.entry3 = Entry(f1, textvariable = self.entryValue3)
                
                self.entryValue4 = StringVar()
                self.entry4 = Entry(f1, textvariable = self.entryValue4)
                
                self.entryValue5 = StringVar()
                self.entry5 = Entry(f1, textvariable = self.entryValue5)
                
                self.entryValue6 = StringVar()
                self.entry6 = Entry(f1, textvariable = self.entryValue6)
                
                self.entry1.grid(row = 1, column = 1)
                self.entry2.grid(row = 2, column = 1)
                self.entry3.grid(row = 3, column = 1)
                self.entry4.grid(row = 4, column = 1)
                self.entry5.grid(row = 5, column = 1)
                self.entry6.grid(row = 6, column = 1)
                
                btn = Button(self, text = '그래프', command = self.draw)
                btn.pack()
                
                self.resultValue = StringVar()
                self.result = Label(self, bg = 'white',
                                    textvariable = self.resultValue)
                self.result.pack()
                
                
        def draw_graph(self, x, y):
            plt.axvline(x=0, color = 'black')   # x, y축 추가
            plt.axhline(y=0, color = 'black')
    
            plt.plot(x, y)
            plt.grid(color='0.8')
            plt.show()
    
    
        def xrange(self, start, final, interval): # x값 범위 입력받아 저장
            numbers = [] 
            while start < final: 
                numbers.append(start) 
                start += interval 
            return numbers 


        def graph_log(self, a, b, c, base, xmin, xmax): 
            if a >= 0:
                if 0 - b >= xmin:
                    xmin = 0 - b + 0.1
            elif a < 0:
                    if 0 - b <= xmax:
                        xmax = 0 - b - 0.1
            x = self.xrange(xmin, xmax, 0.01) 
            y = []
            for t in x: 
                y.append(a * math.log(t + b, base) + c) 
            self.draw_graph(x, y)
                
                
        def draw(self):
            base = float(self.entryValue1.get())
            a = float(self.entryValue2.get())
            b = float(self.entryValue3.get())
            c = float(self.entryValue4.get())
            xmin = float(self.entryValue5.get())
            xmax = float(self.entryValue6.get())
                
            self.graph_log(a,b,c,base,xmin,xmax)



class btn_5(Toplevel):          #두 점 사이의 거리
        def __init__(self):
                Toplevel.__init__(self)

                self.initialize()

        def initialize(self):
                self.configure(background='white')
                title = Label(self, text = "두 점 사이의 거리",
                              font = ("맑은 고딕", "21", 'bold'),
                              height=2,
                              foreground = '#087666',
                              background = 'white')
                title.pack()

                f1 = Frame(self, bg = 'white')
                f1.pack()

                txt1 = Label(f1, text = "첫번째 점",
                             background = 'white')
                txt2 = Label(f1, text = "두번째 점",
                             background = 'white')
                txt3 = Label(f1, text = "좌표 (x, y)",
                             background = 'white')

                txt1.grid(row = 1, column = 0)
                txt2.grid(row = 2, column = 0)
                txt3.grid(row = 0, column = 1)

                self.entryValue1 = StringVar()
                self.entry1 = Entry(f1, textvariable = self.entryValue1)

                self.entryValue2 = StringVar()
                self.entry2 = Entry(f1, textvariable = self.entryValue2)

                self.entry1.grid(row = 1, column = 1)
                self.entry2.grid(row = 2, column = 1)

                btn = Button(self, text = "계산", command = self.Calculate)
                btn.pack()

                self.resultValue = StringVar()
                self.result = Label(self, bg = 'white',
                                    textvariable = self.resultValue)
                self.result.pack()

        def Calculate(self):
                x1, y1 = point.get_float(self.entryValue1.get())
                x2, y2 = point.get_float(self.entryValue2.get())

                result = "두 점 사이의 거리는 %.2f입니다"%point.point_len(x1, x2, y1, y2)
                self.resultValue.set(result)
                

class MainPage(Tk):
        def __init__(self):
                Tk.__init__(self)
                self.title('M  A  T  H')
                self.geometry('400x500')
                self.resizable(False, False)
                self.configure(background='white')

                self.initialize()
                
                
        def initialize(self):           #프로그램 실행 시 첫 화면                              
                lab1 = Label(self, text="M   A   T   H",
                        font = ("맑은 고딕", "21", 'bold'),
                        anchor = 's',
                        height=2,
                        foreground = '#087666',
                        background = 'white')
                        
                lab2 = Label(self, text="수학보조 프로그램",
                        font = ("맑은 고딕", "16", 'bold'),
                        anchor = 'n',
                        height=2,
                        foreground = '#31C9B3',
                        background = 'white')
                lab1.pack()
                lab2.pack()
		
                b1= Button(self, text = "n차 함수 그래프",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID,
                        command = btn_1)

                b2= Button(self, text = "빗변의 길이",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID,
                        command=btn_2)

                b3= Button(self, text = "지수 함수 그래프",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID,
                        command = btn_3)

                b4= Button(self, text = "로그 함수 그래프",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID,
                        command = btn_4)

                b5= Button(self, text = "두 점 사이의 거리",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID,
                        command = btn_5)

                   
                b1.pack(padx=0, pady=5, side = TOP)
                b2.pack(padx=0, pady=5, side = TOP)
                b3.pack(padx=0, pady=5, side = TOP)
                b4.pack(padx=0, pady=5, side = TOP)
                b5.pack(padx=0, pady=5, side = TOP)


window = MainPage()
window.mainloop()
