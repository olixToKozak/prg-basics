
a=1
for i in range(1,8):
    while a < 50:
        print(a ,end=' ')
        a += 7
    
    print()
    a=int(a/a+i)
    