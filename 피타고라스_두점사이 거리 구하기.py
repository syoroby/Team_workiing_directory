##피타고라스 공식##
import math

num1=input("x값 입력:")
num2=input("y값 입력:")
x=float(num1)
y=float(num2)
z=(x*x)+(y*y)

print("z변의 길이는 ->",math.sqrt(z))

##피타고라스 정리를 이용한, 두 점 사이의 거리 구하기##
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
 
a = p2.x - p1.x    # 선 a의 길이
b = p2.y - p1.y    # 선 b의 길이
 
c = math.sqrt((a * a) + (b * b))    # (a * a) + (b * b)의 제곱근을 구함
print(c)    # 42.42640687119285
