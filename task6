# Задача 1

print('Введите количество элементов')
n = int(input())
tmp = []
while n < 1 or n > 10000:
    print('Введите другое значение в диапазоне от 1 до 10 000')
    n = int(input())
else:
    for i in range(n):
        print('Введите значение')
        a = int(input(""))
        tmp.append(a)   

print(tmp)
print(tmp[::-1])

# Задача 2

print('Введите количество элементов')
n = int(input())
while n < 1 or n > 10000:
    print('Введите другое значение в диапазоне от 1 до 10 000')
    n = int(input())


print('Введите числа через пробел')
str = [input().split()]

print(str)
result = []
result = str[-1:] + str[:-1]
print(result)

# Задача 3

m = int(input("Максимальная масса, которую может выдержать лодка: "))
n = int(input("Колличество рыбаков стоящих на берегу реки: "))
mass = []
for i in range(n) :
    i = int(input("Введите массу рыбака: "))
    mass.append(i)
mass.sort()
print(mass)

i, j = 0, n - 1
boat_count = 0
    
while i <= j:
    if mass[i] + mass[j] <= m:
        i += 1
        j -= 1
        
    else: 
        j -= 1
    boat_count += 1  


print(boat_count)
