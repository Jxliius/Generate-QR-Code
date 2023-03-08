import random
import string

def generate_password(length, include_digits, include_punctuation):
    #Generates a random password of specified length.
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Beispielaufruf
password = generate_password(length=5, include_digits=True, include_punctuation=True)
print(password)