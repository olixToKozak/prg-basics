def f(sentences):
    a=''
    for char in sentences:
        if char != ' ':
            a+=char
    return a