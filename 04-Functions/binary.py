def f(binary_number):
    for i in str(binary_number):
        if i != '0' and i != '1':
            return False
    return True