###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
# read the character's code (use ord())
    
# add one to the character's code
    
# replace new character code with its
# corresponding character (use chr())
    
# add encrypted character to encrypted text
 
    
plain_text = 'The early bird catches the worm'
encrypted_text = ''
textnum = 0
for char in plain_text:
    textnum = ord(char)+1
    textchar= chr(textnum)
    encrypted_text= encrypted_text+textchar
print(f'Base text: {plain_text}')
print('Encrypted text:',encrypted_text)