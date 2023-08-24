import random

a = random.randrange(1, 1001, 1)
b = random.randrange(1, 1001, 1)
x = 0
y = 0
sum_num = a + b
prod_num = a * b


for i in range(1, sum_num + 1):
    if (sum_num - i) * i == prod_num:
        x = i
        y = sum_num - i


print(f'Загаданные числа {a}, {b}. Отгаданные числа {x}, {y}')