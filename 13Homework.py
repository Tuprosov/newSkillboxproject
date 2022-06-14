# task 1

def floatnum(num):
  a = num
  count = 0
  if 0 < num < 1:
    while num < 1:
      num *= 10
      count -= 1
  while num // 10 != 0:
    num //= 10
    count += 1
    if num < 10:
      break
  print('Формат плавающей точки: x =', a / 10 ** count, '* 10 **', count)
 
number = float(input('введите положительное число: '))
while number <= 0:
  number = float(input('введите число больше 0!: '))
floatnum(number)

# task 2

def maxnum(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  elif c > a and c > b:
    return c

num1 = float(input('введите число: '))
num2 = float(input('введите число: '))
num3 = float(input('введите число: '))

print('максимум из трёх чисел', maxnum(num1, num2, num3))

# task 3

def revnum(number):
  summ = 0
  if number < 0:
    number * -1
  while number > 0:
    rem = number % 10
    summ = summ * 10 + rem
    number //= 10
  return summ

  
num1 = int(input('введите число 1: '))
num2 = int(input('введите число 2: '))
reverse1 = revnum(num1)
print('первое число наоборот:', reverse1)
reverse2 = revnum(num2)
print('второе число наоборот:', reverse2)
total = reverse1 + reverse2
print('сумма', total)
finalrev = revnum(total)
print('сумма наоборот:', finalrev)

# task 4

exp = input('введите число: ')
num = ''
power = ''
flag = True 
for sym in exp:
  if flag == True:
    if sym != 'e':
      num += sym
    else:
      flag = False
  elif flag == False:
    power += sym
    
print('мантисса:', num, ', порядок:', power)


# task 5

def changednum(number):
  num_count = 0
  temp = number
  while temp > 0:
    num_count += 1
    temp = temp // 10   
  if num_count < 3:
    print("В первом числе меньше трёх цифр.")
  elif num_count < 4:
    print("Вo втором числе меньше трёх цифр.")
  else:
    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return number

def summ(a, b):
  summ = a + b
  return summ
  

  
first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))

changed_1 = changednum(first_n)
print('Изменённое первое число:', changed_1)
changed_2 = changednum(second_n)
print('Изменённое второе число:', changed_2)

print('\nСумма чисел:', summ(changed_1 , changed_2))


# task 6

start = float(input('Введите начальную амплитуду: '))
finish = float(input('Введите амплитуду остановки: '))
count = 0
while start > finish:
  start = start - (start * 8.4 / 100)
  count += 1
print('Маятник считается остановившимся через', count, 'колебаний')

# task 7

d_max = float(input('Ввведите максимально допустимый уровень опасности: '))
check = 0
MIN_NUMBER = 0
MAX_NUMBER = 4
if d_max < 0:
  print('Уровень опасности не может быть меньше 0! Введите снова.')
else:
  x = (MIN_NUMBER + MAX_NUMBER)/2
  d = x**3 - 3*x**2-12*x+10
  while abs(d) > d_max:
    if d < d_max:
      MAX_NUMBER = x
    else:
      MIN_NUMBER = x
    x = (MIN_NUMBER + MAX_NUMBER)/2
    d = x**3 - 3*x**2-12*x+10
print(x)

# task 8

def numerator(numX, n):
  numerator = (-1)**n * numX**(2*n)
  return numerator
  
def factorial(n):
  fact = 1
  if n == 0:
    return fact
  else:
    for num in range(1, 2*n + 1):
      fact *= num
    return fact

precision = float(input('точность: '))
numX = int(input('введите х: '))
result = 0
member = 1
n = 0
while abs(member) > precision:
  member = numerator(numX, n) / factorial(n)
  result += member
  n += 1
  print(result)
print('Сумма ряда =', result)

# task 9

def annuity_cal(c, p, i):
  i /= 100
  k = (i * (1 + i)**p) / ((1 + i)**p - 1)
  annuity = round((k * c), 2)
  return annuity


credit_amount = float(input('сумма кредита: '))
period = int(input('На сколько лет выдан? '))
interest = int(input('Сколько процентов годовых? '))

credit = credit_amount
annuity = annuity_cal(credit_amount, period, interest)
remaining = 0
total_interest = 0
year_count = 0

while True:
  year_count += 1
  print('\nПериод:', year_count)
  print('Остаток долга на начало периода:', credit_amount)
  print('Выплачено процентов:', credit_amount * interest /100)
  print('Выплачено тела кредита:',  annuity - credit_amount * interest/100)
  total_interest += annuity - credit_amount * interest/100
  credit_amount -= annuity - credit_amount * interest/100
  if year_count == 3:
    remaining = credit - total_interest
    print('\nОстаток долга:', remaining)
    new_period = 0
    period_extend = int(input('На сколько лет продлевается договор?: '))
    new_period += period - year_count + period_extend
    year_count = 0
    new_interest = int(input('Увеличение ставки до: '))
    new_annuity = annuity_cal(remaining, new_period, new_interest)
    while year_count != new_period:
      year_count += 1
      print('\nПериод:', year_count)
      print('Остаток долга на начало периода:', remaining)
      print('Выплачено процентов:', remaining * new_interest / 100 )
      print('Выплачено тела кредита:', new_annuity - remaining * new_interest / 100)
      remaining -= new_annuity - remaining * new_interest /100
    break
print('\nОстаток долга:', remaining)