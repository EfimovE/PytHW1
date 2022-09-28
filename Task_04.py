# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def LengthofSegment (x1coord, y1coord, x2coord, y2coord):
    res = round (math.sqrt((x1coord-x2coord)*(x1coord-x2coord) + (y1coord-y2coord)*(y1coord-y2coord)) , 2)
    print (res)

x1 = int (input("X1:  "))
y1 = int (input("Y1:  "))
x2 = int (input("X2:  "))
y2 = int (input("Y2:  "))
LengthofSegment (x1, y1, x2, y2,)

