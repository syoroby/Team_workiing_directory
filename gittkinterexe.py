from tkinter import *

window=Tk()

w = Label(window, text="수학 보조용 프로그램 math입니다.")
w.grid(row=0, column=3)

b1=button = Button(window, text = "n차 함수 그래프")
b1.grid(row=2, column=2)
b2=button = Button(window, text = "피타고라스의 함수")
b2.grid(row=3, column=2)
b3=button = Button(window, text = "지수 함수 그래프")
b3.grid(row=2, column=3)
b4=button = Button(window, text = "향후 추가")
b4.grid(row=3, column=3)
b3=button = Button(window, text = "로그 함수 그래프")
b3.grid(row=2, column=4)
b4=button = Button(window, text = "향후 추가")
b4.grid(row=3, column=4)





window.mainloop()
