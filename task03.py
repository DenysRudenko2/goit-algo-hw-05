import timeit


# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0

    # Створюємо таблицю для пропусків
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    skip = {k: m for k in pattern}

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == -1:
            return i
        i += skip.get(text[i + m - 1], m)
    return -1


# Алгоритм Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    def build_partial_match_table(pattern):
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
            else:
                if j != 0:
                    j = table[j - 1]
                    i -= 1
        return table

    table = build_partial_match_table(pattern)
    m = len(pattern)
    n = len(text)
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1
    return -1


# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, q=101):  # q - просте число
    m = len(pattern)
    n = len(text)
    d = 256  # кількість символів в наборі ASCII
    p = t = 0  # хеш-значення для шаблона і тексту
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


# Читання файлів
with open("1.txt", 'r', encoding='ISO-8859-1') as f1:
    text1 = f1.read()

with open("2.txt", 'r', encoding='ISO-8859-1') as f2:
    text2 = f2.read()

# Вибір підрядків
existing_substring = "алгоритм"  # підрядок, який існує в текстах
non_existing_substring = "невідомий"  # підрядок, якого немає в текстах

# Вимірювання часу для Боєра-Мура
print("Boyer-Moore for existing substring:", timeit.timeit(lambda: boyer_moore(text1, existing_substring), number=1000))
print("Boyer-Moore for non-existing substring:",
      timeit.timeit(lambda: boyer_moore(text1, non_existing_substring), number=1000))

# Вимірювання часу для Кнута-Морріса-Пратта
print("Knuth-Morris-Pratt for existing substring:",
      timeit.timeit(lambda: knuth_morris_pratt(text1, existing_substring), number=1000))
print("Knuth-Morris-Pratt for non-existing substring:",
      timeit.timeit(lambda: knuth_morris_pratt(text1, non_existing_substring), number=1000))

# Вимірювання часу для Рабіна-Карпа
print("Rabin-Karp for existing substring:", timeit.timeit(lambda: rabin_karp(text1, existing_substring), number=1000))
print("Rabin-Karp for non-existing substring:",
      timeit.timeit(lambda: rabin_karp(text1, non_existing_substring), number=1000))
