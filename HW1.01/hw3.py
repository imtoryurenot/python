# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('enter the number of the coordinate plane: '))
if a == 1:
    print('x could be from 1-5 and y also could be from 1-5')
elif a == 2:
    print('x could be from -1 till -5 and y is gonna be from 1-5')
elif a == 3:
    print('x could be from -1 till -5 and y is gonna be from -1 till -5')
elif a == 4:
    print('x could be from 1-5 and y is gonna be from -1 till -5')
else:
    print('this is not gonna')