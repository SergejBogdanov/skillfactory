def binary_search(arr, target):
    """Функция для реализации двоичного поиска в отсортированном массиве."""
    left = 0  # Индекс левой границы
    right = len(arr) - 1  # Индекс правой границы

    while left <= right:
        mid = (left + right) // 2  # Находим середину
        if arr[mid] < target:  # Если элемент в середине меньше целевого
            left = mid + 1  # Ищем справа от середины
        elif arr[mid] > target:  # Если элемент в середине больше целевого
            right = mid - 1  # Ищем слева от середины
        else:  # Если элемент в середине равен целевому
            return mid  # Возвращаем индекс элемента
    return left  # Если не найдено точного совпадения, возвращаем позицию для вставки


def sort_list(lst):
    """Функция для сортировки списка по возрастанию."""
    return sorted(lst)


def main():
    sequence = input("Введите последовательность чисел через пробел: ").strip().split()
    try:
        sequence = [int(num) for num in sequence]  # Преобразуем введенную строку в список чисел
    except ValueError:
        print("Ошибка: в последовательности есть элементы, не являющиеся числами.")
        return

    target = input("Введите любое число: ")
    try:
        target = int(target)  # Преобразуем введенное число в целое число
    except ValueError:
        print("Ошибка: введено число неверного формата.")
        return

    sorted_sequence = sort_list(sequence)  # Сортируем последовательность
    index = binary_search(sorted_sequence, target)  # Находим позицию числа с помощью двоичного поиска

    if index == len(sorted_sequence):  # Если позиция равна длине списка
        print(f"Введенное число {target} больше всех чисел в последовательности.")
    elif index == 0:  # Если позиция равна 0
        print(f"Введенное число {target} меньше всех чисел в последовательности.")
    else:  # В противном случае
        print(f"Позиция числа {target} в отсортированной последовательности: {index}")


if __name__ == "__main__":
    main()
