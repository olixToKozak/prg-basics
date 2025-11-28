def raed_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = raed_file('pets.txt')
lines = file_content.splitlines()
lenlines = len(lines)
a=0
for i in range(lenlines):
    a=+i
print(a)

print(file_content)
#do skonczenia