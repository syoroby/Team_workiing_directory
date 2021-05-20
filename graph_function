import matplotlib.pyplot as plt
import numpy as np

def print_graph (x,y):
    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()
def graph1 (a,b):
    x = np.arange(-10.0,10.01,0.01)   # x의 값（1～10）
    y = a * x ** 3 + b * x ** 2 + c * x + d
    print_graph(x,y)
def graph2 (a,b,c):
    x = np.arange(-10.0,10.01,0.01)   # x의 값（1～10）
    y = a * x ** 2 + b * x  + c
    print_graph(x,y)
def graph3 (a,b,c,d):
    x = np.arange(-10.0,10.01,0.01)   # x의 값（1～10）
    y = a * x ** 3 + b * x ** 2 + c * x + d
    print_graph(x,y)

graph_num = int(input('몇차 그래프를 그릴까요?: '))
if graph_num == 1:
    print("방정식을 'y = ax + b'처럼 정리해주세요.")
    a = int(input('a를 입력해주세요: '))
    b = int(input('b를 입력해주세요: '))
    print('y = {}x + {}의 그래프를 출력하겠습니다.'.format(a,b))
    graph1(a,b)
elif graph_num == 2:
    print("방정식을 'y = ax²+ bx + c'처럼 정리해주세요.")
    a = int(input('a를 입력해주세요: '))
    b = int(input('b를 입력해주세요: '))
    c = int(input('c를 입력해주세요: '))
    print('y = {}x²+ {}x + {}의 그래프를 출력하겠습니다.'.format(a,b,c))
    graph2(a,b,c)
elif graph_num == 3:
    print("방정식을 'y = ax³+ bx²+ cx + d'처럼 정리해주세요.")
    a = int(input('a를 입력해주세요: '))
    b = int(input('b를 입력해주세요: '))
    c = int(input('c를 입력해주세요: '))
    d = int(input('d를 입력해주세요: '))
    print('y = {}x³+ {}x²+ {}x + {}의 그래프를 출력하겠습니다.'.format(a,b,c,d))
    graph3(a,b,c,d)
else:
    print('1차 함수부터 3차 함수까지의 그래프만 그릴 수 있습니다.')
