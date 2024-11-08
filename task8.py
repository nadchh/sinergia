# Задача 1. Вет клиника

pets = dict()

print('Выберите действие')
req = input()
if req == "create":
    print('Введите имя питомца')
    # name_pets = dict()
    # pets[name_pets] = dict()
    name_pets = input()
    pets[name_pets] = dict()
    
    name_pets = {'type' : '', 'old' : 0, 'name_user' : ''}
    
    print('Введите вид питомца')
    # type = input()
    name_pets['type'] = input()
    
    print('Введите возраст питомца')
    name_pets['old'] = int(input())
    
    print('Введите имя владельца')
    name_pets['name_user'] = input()
    
    print(pets.keys())
    print(pets)
    print(name_pets.keys())
    print(name_pets)
else:
    print('Введите корректное действие')


if name_pets['old'] % 10 == 1 and name_pets['old'] % 100 != 11:
    suffix = "год"
elif name_pets['old'] % 10 in [2, 3, 4] and not (name_pets['old'] % 100 in [12, 13, 14]):
    suffix = "года"
else:
    suffix = "лет"
pet_info = {
    "Вид питомца ": name_pets['type'],
    "Возраст питомца ": f"{name_pets['old']} {suffix}",
    "Владелец питомца ": name_pets['name_user']
}
name_pets = pet_info
print(pets)

name_pets.keys()
name_pets.values()
    
# Задача 2

result = {}
for k in range(10, -5, -1):
    result[k] = k ** k
print(result)
