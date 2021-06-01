from tkinter import *

window=Tk()

w = Label(window, text="수학 입니다.")
w.grid(row=0, column=3)

b1=button = Button(window, text = "click")
b1.grid(row=2, column=3)


window.mainloop()
