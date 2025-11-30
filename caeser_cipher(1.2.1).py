# text encryption or decryption or build a caesar cipher

# method --1
def caesar(text, shift, encrypt = True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift > 25 or shift < 1:
        return 'Shift must be an integer between 1 and 25.'
    if not encrypt:
        shift = - shift
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt = False)

text_1 = 'freeCodeCamp'
encrypted_text_1 = encrypt(text_1, 3)
print(encrypted_text_1) # iuhhFrghFdps

text_2 = 'iuhhFrghFdps'
decrypted_text_1 = decrypt(text_2, 3)
print(decrypted_text_1) # freeCodeCamp

text_3 = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text_2 = decrypt(text_3, 13)
print(decrypted_text_2) # Courage is found in unlikely places.

text_4 = 'Courage is found in unlikely places.'
encrypted_text_2 = encrypt(text_4, 13)
print(encrypted_text_2) # Pbhentr vf sbhaq va hayvxryl cynprf.


# method --2
def caesar_1(text, shift):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    shift = shift % 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

encrypted_text = caesar_1("freeCodeCamp", 3) # + shift is used for encryption
print(encrypted_text) # iuhhFrghFdps

decrypted_text = caesar_1(encrypted_text, -3) # - shift is used for decryption
print(decrypted_text) # freeCodeCamp
