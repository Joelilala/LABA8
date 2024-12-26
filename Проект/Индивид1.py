# Пример кортежа чисел
numbers = (1, 3, 2, 5, 4, 6, 7, 5)

def find_peak_triplet(t):
    for i in range(1, len(t) - 1):
        if t[i] > t[i - 1] and t[i] > t[i + 1]:
            return (i - 1, i, i + 1)  # Возвращаем индексы тройки
    return None

result = find_peak_triplet(numbers)

if result:
    print("Номера элементов первой тройки:", result)
else:
    print("Тройка не найдена.")