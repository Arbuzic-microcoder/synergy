# Запрашиваемс параметры прямоугольника
# числа могут быть как int, так и float, логичнее использовать второе для точности расчётов
a, b = map(float, input().split())

area = a * b # вычисление площади
perimeter = (a+b) * 2 #вычесление периметра
# Вывод
print ("Площадь прямоугольника:", area)
print ("Периметр прямоугольника:", perimeter )