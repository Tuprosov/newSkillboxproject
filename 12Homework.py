§# task 1

def summa_n():
  number = int(input('введите число: '))
  sum = 0
  for num in range(1, number + 1):
    sum += num
  print('сумма чисел до', str(number), 'равна', sum)

summa_n()

# task 2

def positive():
  print('число положительное')
def negative():
  print('число отрицательное')
  
def test():
  number = int(input('введите целое число: '))
  if number > 0:
    positive()
  elif number < 0:
    negative()
    
test()


# task 3

def sum(number):
  summ = 0
  while number > 0:
    summ += number % 10
    number //= 10
  print('сумма цифр равна', summ)
  
def maximum(number):
  maxnum = 0
  while number > 0:
    num = number % 10
    if num > maxnum:
      maxnum = num
    number //= 10
  print('макс число: ', maxnum)    
  
def minimum(number):
  num = 9
  while number > 0:
    minnum = number % 10
    if num > minnum:
      num = minnum
    number //= 10
  print('мин число: ', minnum)
  
  
def calculator():
  number = int(input('введите целое число: '))
  choice = int(input('1 - вывести сумму цифр,2 - вывести максимальную цифру,3 - вывести минимальную цифру '))
  if choice == 1:
    sum(number)
  elif choice == 2:
    maximum(number)
  elif choice == 3:
    minimum(number)
    
calculator()

# task 4

def reverse(seqNum):
  for num in range(seqNum):
    num = int(input('введитe число: '))
    sum = 0
    while num > 0:
      rev = num % 10
      sum = sum * 10 + rev
      num //= 10
    print('число наоборот: ', sum)

seqNum = int(input('сколько чисел в последовательности: '))
reverse(seqNum)

# task 5

def count_letters(text):
  countletter = 0
  countnum = 0
  letter = input('Какую букву ищем? ')
  num = input('Какую цифру ищем? ')
  for sym in text:
    if sym == letter:
      countletter += 1
    elif sym == num:
      countnum += 1
  print('Количество цифр ' + str(num) + ':', countnum)
  print('Количество букв ' + str(letter) + ':', countletter)
      
  
text = input('введите текст: ')
count_letters(text)

# task 6

def cordinates(pointX, pointY):
  if -1 <= pointX <= 1 and -1 <= pointY <= 1:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')

pointX = float(input('введите точку X: '))
pointY = float(input('введите точку Y: '))
cordinates(pointX, pointY)

# task 7
num_1 = int(input('введите первое число: '))
num_2 = int(input('введите второе число: '))
summ = num_1 + num_2
sub = abs(num_1 - num_2) 
max = (summ + sub) / 2
min = max - sub
print('малое число: ', min)

# task 8

def gcd(num_1, num_2):
  if num_1 > num_2:
    max = num_1
    min = num_2
  elif num_2 > num_1:
    max = num_2
    min = num_1
  while max % min != 0:
    denom = max % min
    max = min
    min = denom
  print('наибольший общий делитель:', min)

  
num_1 = int(input('введите число: '))
num_2 = int(input('введите число: '))

gcd(num_1, num_2)

# task 9


def rock_paper_scissors():
  import random
  while True:
    choices = ['камень', 'ножницы', 'бумага']
    cpu = random.choice(choices)
    player = None 
    while player not in choices:
      player = (input('камень, ножницы, бумага? '))
      print('\nкомпьютер:', cpu)
      print('игрок: ', player)
    if player == cpu:
      print('ничья!')
    elif player == 'камень' and cpu == 'бумага':
      print('вы проиграли!')
    elif player == 'ножницы' and cpu == 'камень':
      print('вы проиграли!')
    elif player == 'бумага' and cpu == 'ножницы':
      print('вы проиграли!')
    else:
      print('вы выиграли!')
    round = input('еще раз?')
    if round != 'да':
      print('игра завершена!')
      break 

def guess_the_number():
  import random
  compNum = random.randint(1,10)
  player = 0
  while player != compNum:
    player = int(input('угадай число от 1 до 10: '))
  print('Угадал!')
        
  
def mainMenu():
  choice = int(input('1 - камень ножницы бумага \n2 - Угадай число \nвыберите номер игры: '))
  if choice == 1:
    rock_paper_scissors()
  elif choice == 2:
    guess_the_number()
mainMenu()


# Testing git diff
# shahzod testing git branches
# konflikt versiy 01
# conflict of versions 01