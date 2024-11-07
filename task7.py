# Задача 1. Уникальные значения

print('Введите значение')
n = int(input())

while n < 1 or n > 100000:
    print('Введите другое значение в диапазоне от 1 до 10 000')
    n = int(input())
    
print('Введите числа через пробел')
num = list(map(int, input().split()))
num_l = set(num)

print(len(num_l))

# Задача 2. Уникальные числа двух списков

print('Введите количество чисел первого списка')
n1 = int(input())

while n1 < 1 or n1 > 100000:
    print('Введите другое значение в диапазоне от 1 до 10 000')
    n1 = int(input())
    
print('Введите числа первого списка через пробел')
num1 = list(map(int, input().split()))
num_l1 = set(num1)

print('Введите количество чисел второго списка')
n2 = int(input())

while n2 < 1 or n2 > 100000:
    print('Введите другое значение в диапазоне от 1 до 10 000')
    n2 = int(input())
    
print('Введите числа второго списка через пробел')
num2 = list(map(int, input().split()))
num_l2 = set(num2)

print(len(num_l1.union(num_l2)))

# Задача 3. Встречающиеся числа списка

print('Введите числа')
numbers = list(map(int, input().split()))

seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
