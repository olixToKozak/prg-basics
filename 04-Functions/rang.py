def f(x,y):
    count = 0
    for i in range(x,y):
        if i % 2 == 0 and i < 0:
            count +=1
    return count