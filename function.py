import string
import random


class RandomDataUser:

    @staticmethod
    def random_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def random_email(length):
        characters = string.ascii_letters
        email = f'{"".join(random.choice(characters) for _ in range(length))}{random.randint(100,999)}@gmail.com'
        return email