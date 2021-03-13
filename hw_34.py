# Задача 4
# Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.

def my_func_1(x, y):
    return 1 / x ** abs(y)
 
print(my_func_1(5, -10))
 
 
def my_func_2(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x
 
print(my_func_2(2, -2))

