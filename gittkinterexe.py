from tkinter import *
import point

class Button5(Toplevel):
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
                
                
        def initialize(self):                              
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
                        relief = SOLID)

                b2= Button(self, text = "피타고라스의 수",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID)

                b3= Button(self, text = "지수 함수 그래프",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID)

                b4= Button(self, text = "로그 함수 그래프",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID)

                b5= Button(self, text = "두 점 사이의 거리",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID,
                        command = Button5)

                b6= Button(self, text = "연습문제",
                        font = ("맑은 고딕", "10", 'bold'),
                        fg = "#087666",
                        width = 20, height = 2,
                        bg = '#b4dede',
                        relief = SOLID)
                   
                b1.pack(padx=0, pady=5, side = TOP)
                b2.pack(padx=0, pady=5, side = TOP)
                b3.pack(padx=0, pady=5, side = TOP)
                b4.pack(padx=0, pady=5, side = TOP)
                b5.pack(padx=0, pady=5, side = TOP)
                b6.pack(padx=0, pady=5, side = TOP) 


window = MainPage()
window.mainloop()
