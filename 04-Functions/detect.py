def f(detector):
    count = 0
    for i in detector:
        if i == '+':
            count += 1
            if count >=3:
                return True
        elif i =='-':
            count -=1
  
    else:
        return False