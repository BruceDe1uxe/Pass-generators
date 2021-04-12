import random

class PasswordGenerator:
    def __init__(self):
        self.alphabet = '1234567890' \
                        'qwertyuiopasdfghjklzxcvbnm' \
                        'QWERTYUIOPASDFGHJKLZXCVBNM' \
                        '!@#$%^&*()_+'

    def next(self, length=10):
        password = ''
        for i in range(length):
            c = random.choice(self.alphabet)
            password += c
        return password

generator2 = PasswordGenerator()
print(generator2.next())
