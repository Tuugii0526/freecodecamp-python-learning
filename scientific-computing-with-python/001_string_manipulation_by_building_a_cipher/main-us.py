text='may others be happy and peaceful'
custom_key='calm'
def vigenere(message,key,direction=1):
    key_index=0
    alphabet='abcdefghijklmnopqrstuvwxyz'
    final_message=''
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char=key[key_index%len(key)]
            key_index+=1

            #Define the offset and get encrypted/decrypted letter
            offset=alphabet.index(key_char)
            index=alphabet.find(char)
            new_index=(index+offset*direction)%len(alphabet)
            final_message+=alphabet[new_index]
    return final_message
def encrypt(text,key):
    return vigenere(text,key)
def decrypt(text,key):
    return vigenere(text,key,-1)
encryptedText=encrypt(text,custom_key)
print(f'encrypt "{text}":{encrypt(text,custom_key)}\n')
print(f'decrypt "{encryptedText}":{decrypt(encryptedText,custom_key)}')