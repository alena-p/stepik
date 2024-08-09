import random

def is_valid(n, l, r):
  if n.isdigit() and int(n) in range(l, r + 1):
    return True
  else:
    return False

def enter_number(left, right):
  while True:
    num = input(f'Введите число от {left} до {right}: ')
    if is_valid(num, left, right) is False:
      print(f'А может быть все-таки введем целое число от {left} до {right}?')
      continue
    else:
      return int(num)


print('Добро пожаловать в числовую угадайку')

while True:
  print('Введите правую границу диапазона от 2 до 100')
  right_num = enter_number(2, 100)
  random_num = random.randint(1, right_num)
  games = 0
  attempts = 0
  print('Какое число мы загадали?')
  while True:
    guess_num = enter_number(1, right_num)
    if guess_num == random_num:
      print('Вы угадали, поздравляем!')
      attempts += 1
      games += 1
      break
    elif guess_num < random_num:
      print('Ваше число меньше загаданного, попробуйте еще разок')
      attempts += 1
      continue
    elif guess_num > random_num:
      print('Ваше число больше загаданного, попробуйте еще разок')
      attempts += 1
      continue
  print(f"Количество попыток, за которые вы угадали - {attempts}")
  attempts = 0
  if games > 0:
    print('Хотиет сыграть еще? Y/N')
    answer = input()
    if answer == 'Y':
      continue
    else:
      break
  else:
    break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')