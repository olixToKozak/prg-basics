def f(text):
    stext=''
    count=0
    for char in text:
        count +=1
        if count < len(text):
            stext += char + '-'
        else:
            stext += char
    return stext