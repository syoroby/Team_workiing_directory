import matplotlib.pyplot as plt

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

def graph1(a, b, xmin, xmax): 
    x = xrange(xmin, xmax, 0.01) 
    y = [] 
    for t in x: 
        y.append(a * t + b) 
    draw_graph(x, y)

def graph2(a, b, c, xmin, xmax): 
    x = xrange(xmin, xmax, 0.01) 
    y = [] 
    for t in x: 
        y.append(a * t ** 2 + b * t + c) 
    draw_graph(x, y)

def graph3(a, b, c, d, xmin, xmax): 
    x = xrange(xmin, xmax, 0.01) 
    y = [] 
    for t in x: 
        y.append(a * t ** 3 + b * t ** 2 + c * t + d) 
    draw_graph(x, y) 


graph_num = int(input('몇차 그래프를 그릴까요? (1, 2, 3) : '))

if graph_num == 1:
    print("방정식을 'y = ax + b'처럼 정리해주세요.")
    a = float(input('a를 입력해주세요: '))                                 # 실수 범위에서 입력받을 수 있도록 수정
    b = float(input('b를 입력해주세요: '))
    xmin = float(input('정의역의 최소값을 입력하세요 : '))       # x값의 범위를 입력받을 수 있도록 수정
    xmax = float(input('정의역의 최대값을 입력하세요 : '))

    print('y = {}x + {}의 그래프를 출력하겠습니다.'.format(a,b))
    graph1(a, b, xmin, xmax)

elif graph_num == 2:
    print("방정식을 'y = ax²+ bx + c'처럼 정리해주세요.")
    a = float(input('a를 입력해주세요: '))
    b = float(input('b를 입력해주세요: '))
    c = float(input('c를 입력해주세요: '))
    xmin = float(input('정의역의 최소값을 입력하세요 : '))
    xmax = float(input('정의역의 최대값을 입력하세요 : '))

    print('y = {}x²+ {}x + {}의 그래프를 출력하겠습니다.'.format(a,b,c))
    graph2(a, b, c, xmin, xmax)
    
elif graph_num == 3:
    print("방정식을 'y = ax³+ bx²+ cx + d'처럼 정리해주세요.")
    a = float(input('a를 입력해주세요: '))
    b = float(input('b를 입력해주세요: '))
    c = float(input('c를 입력해주세요: '))
    d = float(input('d를 입력해주세요: '))
    xmin = float(input('정의역의 최소값을 입력하세요 : '))
    xmax = float(input('정의역의 최대값을 입력하세요 : '))

    print('y = {}x³+ {}x²+ {}x + {}의 그래프를 출력하겠습니다.'.format(a,b,c,d))
    graph3(a, b, c, d, xmin, xmax)
    
else:
    print('1차 함수부터 3차 함수까지의 그래프만 그릴 수 있습니다.')
