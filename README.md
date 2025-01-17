# goit-algo-hw-05

# Порівняння ефективності алгоритмів пошуку підрядка

## Результати вимірювання часу для кожного алгоритму:

### Для існуючого підрядка:
- **Boyer-Moore**: 0.2968603 сек
- **Knuth-Morris-Pratt**: 1.6509258 сек
- **Rabin-Karp**: 2.2805912 сек

### Для неіснуючого підрядка:
- **Boyer-Moore**: 0.2641995 сек
- **Knuth-Morris-Pratt**: 1.6349219 сек
- **Rabin-Karp**: 2.2678102 сек

## Висновки:

1. **Boyer-Moore** виявився найшвидшим алгоритмом як для існуючого, так і для неіснуючого підрядка. Його час виконання був найнижчим у порівнянні з іншими алгоритмами.
   
2. **Knuth-Morris-Pratt** показав середню продуктивність, значно перевищивши час виконання Boyer-Moore, але залишився швидшим за Рабіна-Карпа.

3. **Rabin-Karp** був найповільнішим серед усіх алгоритмів для обох типів підрядків, особливо для існуючого підрядка, що свідчить про його меншу ефективність у порівнянні з іншими методами для даного випадку.

### Загальний висновок:
Алгоритм **Boyer-Moore** є найбільш оптимальним для швидкого пошуку підрядків у тексті серед трьох розглянутих, як для існуючих, так і для неіснуючих підрядків.
"""