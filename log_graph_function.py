import matplotlib.pyplot as plt
import math

def draw_graph(x, y):
    plt.axvline(x=0, color = 'black')   # x, y축 추가
    plt.axhline(y=0, color = 'black')
    
    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()
    
    
def xrange(start, final, interval): # x값 범위 입력받아 저장
    numbers = [] 
    while start < final: 
        numbers.append(start) 
        start += interval 
    return numbers 

def graph_log(a, b, c, base, xmin, xmax): 
    if a >= 0:
        if 0 - b >= xmin:
            xmin = 0 - b + 0.1
    elif a < 0:
        if 0 - b <= xmax:
            xmax = 0 - b - 0.1
    x = xrange(xmin, xmax, 0.01) 
    y = []
    for t in x: 
        y.append(a * math.log(t + b, base) + c) 
    draw_graph(x, y)
    
print("방정식을 'y = alog(x+b)+c'처럼 정리해주세요.")
a = float(input('a를 입력해주세요: ')) 
base = float(input('로그의 밑을 입력해주세요: '))
b = float(input('b를 입력해주세요: ')) 
c = float(input('c를 입력해주세요: '))
xmin = float(input('정의역의 최소값을 입력하세요 : '))       # x값의 범위를 입력받을 수 있도록 수정
xmax = float(input('정의역의 최대값을 입력하세요 : '))

print('y = {}log{}(x+{})+{}의 그래프를 출력하겠습니다.'.format(a,base,b,c))
graph_log(a, b, c,  base, xmin, xmax)