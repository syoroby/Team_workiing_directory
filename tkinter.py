from tkinter import *
import tkinter
import tkinter as tk

def btn1_button():
    root1=tkinter.Tk()
    root1.grab_set()
    root1.title("이름")
    label=tkinter.Label(root1, text="이름")
    lbl = Label(root1, text = "이름")
    lbl.grid(row = 0, column = 0)
    txt1 = Entry(root1)
    txt1.grid(row = 0, column = 1)

    lb2 = Label(root1, text = "이름")
    lb2.grid(row = 1, column = 0)
    txt2 = Entry(root1)
    txt2.grid(row = 1, column = 1)

    btn = tk.Button(root1, text = "Ok", width = 15)
    btn.grid(row = 3, column = 1)

    root1.mainloop()

window=tkinter.Tk()
#윈도우 창의 제목
window.title("math")
window

#레이블 생성
label = tkinter.Label(window, text="수학 보조용 프로그램 math입니다.", fg="black", bg="yellow", font=(20))



label.grid()

b1=tk.Button(window, text = "n차 함수 그래프",command=btn1_button, bg="lightgreen")
b1.grid(row=4, column=2)
b2=button = Button(window, text = "피타고라스의 함수", bg="lightgreen")
b2.grid(row=3, column=2)
