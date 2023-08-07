# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е.
# не меньше заданного минимума и не больше заданного максимума)
import random 

n=(int(input("Введите число для n элементов для первого множества: ")))
list_one = [random.randint(-10, 11) for x in range(1, n+1)]
print(list_one)

list_total = []
min_value = 6
max_value = 10

for i in range(len(list_one)):
    if list_one[i] >= min_value and list_one[i] <= max_value:
        list_total.append(i)
print(list_total)