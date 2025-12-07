def f(number, even):
    a=0
    if even == True:
        for i in str(number):
            if int(i) % 2 == 0:
                a += int(i)
        
    elif even == False:
        for i in str(number):
            if int(i) % 2 !=0:
                a +=int(i)

    return a