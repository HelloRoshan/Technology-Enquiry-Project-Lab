import math
from turtle import width


def circleArea():
    cirRadius = float(input('Enter a radius'))
    cirArea = math.pi * pow(cirRadius, 2)
    print('Circle Area is ', cirArea)
    roundedValue = round(cirArea, 2)
    print('Which round off has a value of', roundedValue)


def rectangleArea(length, width):
    rectArea = length * width
    print(rectArea)


def squareArea(sideLength):
    rectangleArea(sideLength, sideLength)


squareArea(5)
