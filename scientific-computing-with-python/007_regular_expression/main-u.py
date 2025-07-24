# Бидний зорилго бол тодорхой нөхцөлүүдийг хангасан пассворд үүсгэх юм . 
import string
import re
import secrets
def generate_password(length=16,nums=1,special_chars=1,lowercase=1,uppercase=1):
    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    all_letters=letters+digits+symbols
   
    while True:
        password=''
        for _ in range(length):
            password+=secrets.choice(all_letters)
            
        constraints=[
            (nums,r'\d'),
            (special_chars,fr'[{symbols}]'),
            (uppercase,r'[A-Z]'),
            (lowercase,r'[a-z]')
        ]
        if all( constraint <= len(re.findall(pattern,password)) for constraint, pattern in constraints):
            break
    return password
if __name__ == '__main__':
    password=generate_password(nums=3)
    print('Password:',password)