from tkinter import *

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

window=Tk()
window.title('M  A  T  H')
window.geometry('400x500')
window.resizable(False, False)
window.configure(background='white')

w1 = Label(window, text="M   A   T   H",
          font = ("맑은 고딕", "21", 'bold'),
           anchor = 's',
          height=2,
          foreground = '#087666',
          background = 'white')
w2 = Label(window, text="수학보조 프로그램",
          font = ("맑은 고딕", "16", 'bold'),
           anchor = 'n',
           height=2,
           foreground = '#31C9B3',
           background = 'white')

w1.pack()
w2.pack()

b1= Button(window, text = "n차 함수 그래프",
           font = ("맑은 고딕", "10", 'bold'),
           fg = "#087666",
           width = 20, height = 2,
           bg = '#b4dede',
           relief = SOLID)

b2= Button(window, text = "피타고라스의 수",
           font = ("맑은 고딕", "10", 'bold'),
           fg = "#087666",
           width = 20, height = 2,
           bg = '#b4dede',
           relief = SOLID)

b3= Button(window, text = "지수 함수 그래프",
           font = ("맑은 고딕", "10", 'bold'),
           fg = "#087666",
           width = 20, height = 2,
           bg = '#b4dede',
           relief = SOLID)

b4= Button(window, text = "로그 함수 그래프",
           font = ("맑은 고딕", "10", 'bold'),
           fg = "#087666",
           width = 20, height = 2,
           bg = '#b4dede',
           relief = SOLID)

b5= Button(window, text = "두 점 사이의 거리",
           font = ("맑은 고딕", "10", 'bold'),
           fg = "#087666",
           width = 20, height = 2,
           bg = '#b4dede',
           relief = SOLID,
           command = Button5)

b6= Button(window, text = "연습문제",
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





window.mainloop()
