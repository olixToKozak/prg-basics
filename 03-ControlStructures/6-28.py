a = 0
b = 1

for i in range(20):
    print(a, end=' ')
    fiba = b
    fibb = a + b
    a = fiba
    b = fibb