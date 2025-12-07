def f(product_code):
    product_code=str(product_code)
    count = 0
    reminder=0
    last=0
    for i in product_code:
        count+=1
        if count <len(product_code):
            reminder+=int(i)
        else:
            last += int(i)
    if reminder%7==last:
        return True
    else:
        return False