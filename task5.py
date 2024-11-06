# Задача 1

print('Введите строку')
a = input()
x = len(a)

b = a[x::-1]
print(b)

if a == b:
    print('yes')
else:
    print('no')

# Задача 2

q = input()
print(' '.join(q.split()))
