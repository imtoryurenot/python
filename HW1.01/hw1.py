# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

d = int(input('Enter the day number to check if its the weekend: '))
if d > 0 and d < 6:
    print('it is not a weekend')
elif d > 5 and d < 8:
    print('it is the weekend!')
else:
    print('this day does not exist')