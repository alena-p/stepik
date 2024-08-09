import random


def generate_password(length, symbols):
    password = ""
    for i in range(0, length):
        password = password + symbols[random.randrange(len(symbols))]
    return password


DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"

chars = ""

print("Привет, для генерации нужного пароля ответьте на несколько вопросов.")
passwords_count = int(input("Количество паролей для генерации? "))
passwords_length = int(input("Длина одного пароля? "))
digits_include = input("Включать ли цифры 0123456789? Y/N ")
low_let_include = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Y/N ")
up_let_include = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Y/N ")
symbols_include = input("Включать ли символы !#$%&*+-=?@^_? Y/N ")
symbols_exclude = input("Исключать ли неоднозначные символы il1Lo0O? Y/N ")

if digits_include == "Y":
    chars = chars + DIGITS
if low_let_include == "Y":
    chars = chars + LOWERCASE_LETTERS
if up_let_include == "Y":
    chars = chars + UPPERCASE_LETTERS
if symbols_include == "Y":
    chars = chars + PUNCTUATION
if symbols_exclude == "Y":
    symbols_exclude = "il1Lo0O"
    for i in symbols_exclude:
        chars = chars.replace(i, "")

for i in range(0, passwords_count):
    print(f"Пароль {i + 1}: {generate_password(passwords_length, chars)}")
