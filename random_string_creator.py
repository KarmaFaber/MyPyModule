import string
import random

#random character string: size=6, capital: digit + letters
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    

#random password generator: size=10, digits+punct+ascii_letters
def password_generator():
    password=[]
    for i in range(5):
        alpha=random.choice(string.ascii_letters)
        symbol=random.choice(string.punctuation)
        numbers=random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
    return "".join(str(x)for x in password)
       


