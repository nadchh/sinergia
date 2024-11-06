#площадь и периметр треугольника

print('Ведите стороны треугольника')

print('первая сторона')
a = int(input())

print('вторая сторона')
b = int(input())

print('третья сторона')
c = int(input())

p = (a + b + c)/2
# print(p)
p = p*(p-a)*(p-b)*(p-c)
# print(p)
s = p ** (1/2)
# print(p)

P = a + b + c

print('Площадь треугольника равна', s)
print('Периметр треугольника равен', P)

# Задание 2 пятизначное число

print('Введите пятизначение число')
x = int(input())

edin = x % 10
# print(edin)

desat = x % 100
desat = desat // 10
# print(desat)

sot = x % 1000
sot = sot // 100
# print(sot)

tisa = x % 10000
tisa = tisa // 1000
# print(tisa)

desattisa = x % 100000
desattisa = desattisa // 10000
# print(desattisa)

alg1 = desat ** edin
# print(alg1)
alg2 = alg1 * sot
# print(alg2)
alg3 = desattisa - tisa
# print(alg3)
alg4 = alg2 / alg3
print(alg4)
