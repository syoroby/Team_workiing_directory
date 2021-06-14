##피타고라스 공식##
import math

print("[[삼각형 변의 길이 구하기]]")

v1 = input("빗변의 길이를 알고 있나요? (Y/N) >> ")

if v1 == "Y" or v1 == "y":
    x = float(input("빗변의 길이를 입력하세요 >> "))
    y = float(input("나머지 한 변의 길이를 입력하세요 >> "))

    z = (x*x) - (y*y)

    print("나머지 변의 길이는 %.3f입니다."%math.sqrt(z))

elif v1 == "N" or v1 == "n":
    x=float(input("밑변의 길이를 입력하세요 >> "))
    y=float(input("높이를 입력하세요 >> "))

    z=(x*x)+(y*y)

    print("빗변의 길이는 %.3f입니다."%math.sqrt(z))  #빗변의 길이 출력

else :
    print("잘못된 입력입니다.")

##피타고라스 삼각_리스트 활용##
print("[[피타고라스 정리를 만족하는 조합]]")

new_list=[]
for x in range(1,30):
    for y in range(x,30):
        for z in range(y,30):
            if x**2 + y**2 == z**2:
                new_list.append((x,y,z))
                
for i in range(0,len(new_list)):    #엔터로 구분하여 가독성 향상
               print(new_list[i])

##피타고라스 정리를 이용한, 두 점 사이의 거리 구하기##

print("[[두 점 사이의 거리 구하기]]")

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

t1, t2 = map(float, input("첫번째 점의 좌표를 입력하세요 (x, y) >> ").split(",")) #좌표를 입력받는 형식으로 수정
t3, t4 = map(float, input("두번째 점의 좌표를 입력하세요 (x, y) >> ").split(","))

p1 = Point2D(t1, t2)    # 점1
p2 = Point2D(t3, t4)   # 점2
 
a = p2.x - p1.x    # 선 a의 길이
b = p2.y - p1.y    # 선 b의 길이
 
c = math.sqrt((a * a) + (b * b))    # (a * a) + (b * b)의 제곱근을 구함
print("두 점의 거리는 %d 입니다."%c)   
