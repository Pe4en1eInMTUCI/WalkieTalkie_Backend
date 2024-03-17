##from random import randint
##random_code=''
##for i in range(6):
##    random_code+=str(randint(0,9))
##print(random_code)
from random import randint
def random_code():
    code=""
    for i in range(6):
        code+=str(randint(0, 9))
    return code
print(random_code()) 
