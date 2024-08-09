# def draw_box():
#     for i in range(14):
#         if 0 < i < 13:
#             print(f'*{" "*8}*')
#         else:
#             print('*' * 10)
#
#
# draw_box()

# def find_all(target, symbol):
#     inputs = []
#     chars = target.split()
#     for i in range(0, len(chars)):
#         if chars[i] == symbol:
#             inputs.append(i)
#     return inputs
#
# # считываем данные
# s = 'abcdabcaaa'
# char = 'a'

# # вызываем функцию
# print(find_all(s, char))

# объявление функции
# def is_prime(num):
#     flag = True
#
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             flag == False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
# # считываем данные
# n = int(input())


# # вызываем функцию
# print(is_prime(n))

# def is_one_away(word1, word2):
#     chars1 = list(word1)
#     chars2 = list(word2)
#
#     if len(word1) != len(word2) or chars1.sorted() == chars2.sorted():
#         return False
#
#     i = 0
#     while len(chars1) > i:
#         if chars1[i] in chars2:
#             del chars1[i]
#             del chars2[i]
#         else:
#             i += 1
#
#     if len(chars1) == len(chars2) == 1:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# txt1 = 'aab'
# txt2 = 'aba'
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

# def is_correct_bracket(text):
#     array = list(text)
#     left = '('
#     right = ')'
#     count = 0
#     i = 0
#
#     while len(array) > 0 and i <= len(array) - 1:
#         if array[0] == right:
#             return False
#
#         if array[i] == left:
#             count += 1
#         else:
#             count -= 1
#             if count == 0:
#                 array = array[i + 1:]
#                 i = 0
#                 continue
#         i += 1
#
#     if count == 0:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# txt = '()(())()((())((()))()(())'
#
# # вызываем функцию
# print(is_correct_bracket(txt))

# def convert_to_python_case(text):
#     chars = list(text)
#
#     chars.insert(0, chars[0].lower())
#
#     i = 1
#     while i < len(chars):
#         if chars[i].isupper():
#             chars[i].lower()
#         i += 1
#
#     return ''.join(chars)
#
#
# # считываем данные
# txt = 'ThisIsCamelCased'
#
# # вызываем функцию
# print(convert_to_python_case(txt))
#
# def draw_triangle():
#     height = 8
#     for i in range(0, 8):
#         print(f'{" "*(height - 1 - i)}{"*" * (2 * i + 1)}')
#
# # основная программа
# # draw_triangle()  # вызов функции
#
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
#
# # объявление функции
# def compute_binom(n, k):
#     result = factorial(n) / (factorial(k) * factorial(n - k))
#     return result
#
# # считываем данные
# n = 1
# k = 1
#
# # вызываем функцию
# print(compute_binom(n, k))

def number_to_words(num):
    to_10 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    of_20 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    ten_20 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
              'семнадцать', 'восемнадцать', 'девятнадцать']

    if num // 10 == 0:
        return to_10[num - 1]
    elif num // 10 == 1:
        return ten_20[num - 10]
    elif num // 10 > 1:
        if num % 10 == 0:
            return of_20[num // 10 - 2]
        else:
            return f'{of_20[num // 10 - 1]} {to_10[num % 10 - 1]}'


# считываем данные
n = 30

# вызываем функцию
print(number_to_words(n))