def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None  # Ініціалізуємо змінну для "верхньої межі"

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])  # Якщо знайшли точне значення
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]  # Оновлюємо "верхню межу"
            right = mid - 1

    # Після завершення циклу повертаємо кількість ітерацій і "верхню межу"
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]  # Якщо target більший за всі елементи, беремо лівий елемент

    return (iterations, upper_bound)

# Тестуємо функцію
sorted_array = [0.5, 1.3, 2.7, 3.9, 5.2, 6.8, 8.4, 9.7]
target_value = 4.0

result = binary_search(sorted_array, target_value)
print(result)  # Виведе, наприклад, (3, 5.2)
