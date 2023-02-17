# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21 # 
# 
# почему-то очень долго сидела над решением и сначала сделала одно,
# а потом стала копать гугл и нашла возможность интереснее 

#первое:

# a = int(input('Enter x1-coordinate on the graph: '))
# b = int(input('Enter y1-coordinate on the graph: '))
# c = int(input('Enter x2-coordinate on the graph: '))
# d = int(input('Enter y2-coordinate on the graph: '))
# f = (c - a) ** 2
# g = (d - b) ** 2
# h = round((f + g) ** 0.5, 2)

# print(h)

#второе интереснее:

x1, y1 = map(int, input('x-coordinate and y-coordinate (x, y): ').split())
x2, y2 = map(int, input('x-coordinate and y-coordinate (x, y): ').split())

S = round(((x2 - x1)**2 + (y2 - y1)**2)** 0.5, 2) 

print(S)

#хотелось бы отметить, что во всех случаях, кроме первого округление работает верно)