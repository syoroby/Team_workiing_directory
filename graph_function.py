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
