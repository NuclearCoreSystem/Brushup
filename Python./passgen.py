import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Password Length?"))
print("Here you go:", generate_password(length))