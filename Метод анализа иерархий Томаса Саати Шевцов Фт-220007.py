def get_input():
    # Запрос ввода количества критериев
    while True:
        try:
            n = int(input("Введите количество критериев: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка ввода. Введите положительное целое число.")

    # Запрос ввода данных попарного сравнения критериев
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                while True:
                    try:
                        value = float(input(f"Введите коэффициент сравнения между критерием {i+1} и критерием {j+1}: "))
                        if value <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Ошибка ввода. Введите положительное число.")
                row.append(value)
        matrix.append(row)

    return matrix


def calculate_weights(matrix):
    # Вычисление весовых коэффициентов
    n = len(matrix)
    weights = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= matrix[i][j] ** (1/n)
        weights.append(product)

    # Нормализация весовых коэффициентов
    sum_weights = sum(weights)
    normalized_weights = [weight / sum_weights for weight in weights]

    return normalized_weights


def main():
    matrix = get_input()
    weights = calculate_weights(matrix)

    # Вывод весовых коэффициентов
    for weight in weights:
        print(f"{weight:.2f}")


if __name__ == "__main__":
    main()
