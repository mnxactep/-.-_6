import numpy as np

while True:
    try:
        num_criteria = int(input("Введите кол-во критериев: "))
        break
    except ValueError:
        print('Неверное значение критерия')

s_matrix = np.zeros((num_criteria, num_criteria))  # Создаём матрицу нулей

# Заполняем матрицу коэффициентами сравнений
a = 1  # счётчик для пропуска уже заполненных значений
for i in range(a, num_criteria + 1):
    for j in range(a + 1, num_criteria + 1):
        while True:
            try:
                # Заполняем каждый элемент строки матрицы
                s_matrix[i - 1][j - 1] = round(float(input('Введите сравнение К{0}-К{1}:'.format(i, j))), 3)
                break
            except ValueError:
                print('Неверное значение критерия')

        # Заполняем ячейки для обратного отношения (К1-К2 -> К2-К1)
        s_matrix[j - 1][i - 1] = round(1 / s_matrix[i - 1][j - 1], 2)

    a += 1

# Создаём список сумм строки
comp_list = [round(sum(row), 2) for row in s_matrix]
out_list = [round(n / sum(comp_list), 2) for n in comp_list]

if sum(out_list) != 1.0:
    index = out_list.index(max(out_list))
    k = sum(out_list) - 1.0
    out_list[index] -= round(k, 2)

print('Весовые коэффициенты')
for weight in out_list:
    print(weight, end=' ')
