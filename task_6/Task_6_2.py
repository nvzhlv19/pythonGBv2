#  Задача 32:
#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

this_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
len_this_list = len(this_list)
this_list_index = []
max_value = 0
min_value = -10
for i in this_list:
    if min_value < i < max_value:
        this_list_index.append(this_list.index(i))

print(this_list_index)

