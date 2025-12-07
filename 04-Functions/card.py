def hide(card_number):
    count = 0
    a = ''
    for i in str(card_number):
        count+=1
        if count >2 and count <13:
            i = '*'
        else:
            i = i
        a += i 
    return a