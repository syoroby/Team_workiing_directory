from tkinter import *


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
           relief = SOLID)

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
