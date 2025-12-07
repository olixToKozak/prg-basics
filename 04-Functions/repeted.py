def f(number):
    total=0
    number=str(number)
    for i in number:
        if number.count(i) > 1:
            total += int(i) 
    return total