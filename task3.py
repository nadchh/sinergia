#Задание 1 (строки-описания чисел)

print('Введите число')
x = int(input())
ch = x % 2
print(ch)

if x == 0:
    print('ваше число нолевое')
elif x > 0 & ch == 1:
    print('Ваше число положительное и четное')
elif x > 0 & ch == 0:
    print('Ваше число положительное и нечетное')
elif x < 0 & ch == 0:
    print('Ваше число отрицательное и четное')
else:
    print('Ваше число отрицательное и нечетное')


# Задание 2 (количество гласных и согласных букв)

print('Введите слово латинскими буквами')

world = input()
letter = list(world)
index = 0

a = 0
e = 0
i = 0
o = 0
u = 0

gl = 0

while index < len(world):
    if letter[index] == 'a':
        gl += 1
        a += 1
    elif letter[index] == 'e':
        gl += 1
        e += 1
    elif letter[index] == 'i':
        gl += 1
        i += 1
    elif letter[index] == 'o':
        gl += 1
        o += 1
    elif letter[index] == 'u':
        gl += 1
        u += 1
    
    index += 1

print ('Гласных букв в слове "', world, '": ', gl)
print ('Букв в слове "a": ', a)
print ('Букв в слове "e": ', e)
print ('Букв в слове "i": ', i)
print ('Букв в слове "o": ', o)
print ('Букв в слове "u": ', u)

# Задача 3 (инвесторы)

print('Введите минимальную сумму вложений')
minX = int(input())

print('Майкл может инвестировать:')
a = int(input())
print(a, ' долларов')

print('Иван может инвестировать:')
b = int(input())
print(b, ' долларов')

c = a + b

if minX <= a and minX <= b:
    print('2')
elif minX <= a and minX > b:
    print('Mike')
elif minX > a and minX <= b:
    print('Ivan')
elif minX <= c:
    print('1')
else:
    print('0')


