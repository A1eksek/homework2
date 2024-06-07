try:
    a = int(input("Введите делимоме"))
    b = int(input("Введите делитель"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("На ноль делить нельзя")

######
try:
    a = int(input("Введите число"))
except ValueError:
    print("Вы ввели не число")
#####

try:
    str_a = '50'
    b = 10
    c = str_a + b
    print (c)
except TypeError:
    print("преобразования строки в число")