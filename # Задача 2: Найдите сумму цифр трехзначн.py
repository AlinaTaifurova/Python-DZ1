# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# number = int(input)
# sum = 0
# for digit in number:
# sum += int(digit)
# print(sum)

num = int(input("Введите трехзначное число: "))
sum = 0
if num <= 99 or num >= 1000:
    print('Ввели не трехзначное число!')
else:
    a = num // 100
    b = num % 100 // 10
    c = num % 10
    print(f'{a + b + c} ({a} + {b} + {c})')