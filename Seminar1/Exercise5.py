# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
import math


def distance(a, b, c, d):
    return math.sqrt((a - c)**2 + (b - d)**2)


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
print(distance(x1, y1, x2, y2))
