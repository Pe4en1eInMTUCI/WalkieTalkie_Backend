
from random import randint


def random_code():
    code = ""
    for i in range(6):
        code += str(randint(0, 9))
    return str(code)

