plik = open('abc.txt')
content = plik.read()
plik.close()

with open('abc.txt',"c") as plik:
    content=plik.read()
