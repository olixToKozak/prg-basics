def f(name):
    words = name.split()
    acro = ''
    for char in words:
        acro += char[0]
    return acro