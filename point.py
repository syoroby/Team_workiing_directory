##피타고라스 정리를 이용한, 두 점 사이의 거리 구하기##
import math

def get_float(text):
    return map(float,text.split(","))

def point_len(x1, x2, y1, y2):
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt((a * a) + (b * b))

    return c

