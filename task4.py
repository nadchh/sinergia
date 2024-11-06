# Задача 1 

print('введите количство вводимых далее чисел')
n = int(input())
null = 0
print('введите числа')
while n > 0:
    n -= 1
    x = int(input())
    if x == 0:
        null += 1
else:
    print('количество чисел, равных 0: ', null)    
    
# Задача 2

print('введите число')
x = int(input())
kolvo = 0
index = 1

if x <= 2e9:
    while index <= x:
        if x % index == 0:
            kolvo += 1
            print(kolvo)
        index += 1
    
print(kolvo)

# Задача 3

print('введите число a')
a = int(input())
print('введите число b')
b = int(input())
kol = 0
if a <= b:
    while a <= b:
        if a % 2 == 0:
            kol += 1
            print(a)
        a += 1
    print(kol)       
else:
    print('числа должны быть соблюдать условие a<=b')    
