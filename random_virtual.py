import os

from random import randint

number = randint(1, 3)
num = str(number)
os.system('python3 virtual_users/virtual_user' + num + '.py')
