
###################################################################################
#Printing letters up to specified char
###################################################################################

def letters_up_to_char(long_word, char):
    new = ''
    for letter in long_word:
        if letter != char:
            new += letter
        else:
            return new

print letters_up_to_char('coderoxthesox', 'x')
print letters_up_to_char('abcdefghijklmnop', 'f')