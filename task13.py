import random

matrix1 = []

for i in range(10):
    row = [] 
    for j in range(10):
        row.append(random.randint(-99, 99))
    matrix1.append(row) 

for row in matrix1:
    print(row)
    
print()
matrix2 = []

for i in range(10):
    row = [] 
    for j in range(10):
        row.append(random.randint(-99, 99))
    matrix2.append(row) 

for row in matrix2:
    print(row)

print()

result = [] 
for i in range(10):
    row = [] 
    for j in range(10):
        row.append(random.randint(-99, 99))
    result.append(row) 
  
x = 10
y = 10

for i in range(x):
    for j in range(y):
        a = matrix1[i][j] + matrix2[i][j]
        result[i][j] = a
        
    
for row in result:
    print(row)
