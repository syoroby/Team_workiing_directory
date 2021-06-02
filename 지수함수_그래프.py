##증가하는 지수함수 그래프##
import numpy as np
import matplotlib.pyplot as plt

def jisu(start_x, end_x, under):
    x = np.arange(start_x, end_x, (end_x-start_x)/100)
    line = plt.plot(x, under**x)
    plt.setp(line, color='r', linewidth=3.0)
    plt.show()

x1 = float(input('x좌표의 시작점을 입력해주세요: '))
x2 = float(input('x좌표의 끝점을 입력해주세요: '))
under_ = float(input('밑을 입력해주세요: '))
jisu(x1,x2,under_)