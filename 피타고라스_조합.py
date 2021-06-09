##피타고라스 공식##
import math

num1=input("x값 입력:")
num2=input("y값 입력:")
x=float(num1)
y=float(num2)
z=(x*x)+(y*y)

print("z변의 길이는 ->",math.sqrt(z))

##피타고라스 삼각_리스트 활용##
new_list=[]
for x in range(1,30):
    for y in range(x,30):
        for z in range(y,30):
            if x**2 + y**2 == z**2:
                new_list.append((x,y,z))

print(new_list)


