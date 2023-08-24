import random

n = random.randrange(0, 101,2) # случайное число монеток
coint_list = []
print(f'Всего монет {n}')

for i in range(1, n + 1):
    coint_list.append(random.randrange(0, 2, 1)) # создаем случайный список моенток 0 или 1
sum_coint = sum(coint_list)

n = n - sum_coint
print(f'Количество монеток гербом вверх {n}, количество монеток решкой верх {sum_coint}')

if n < sum_coint:
    print(f'Минимальное число монеток которое нужно перевернуть чтобы они были одной стороной равно {n}')
else:
    print(f'Минимальное число монеток которое нужно перевернуть чтобы они были одной стороной равно {sum_coint}')




