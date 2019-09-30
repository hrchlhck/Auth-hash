import itertools
import string
import hashlib
import time
from data import *

characters = string.digits
credentials = 'credentials.txt'

def crack(target, chars,size=4):
    cracked = ''
    passwords = []
    data = get_credentials(target)
    for j in range(len(data)):
        for i in itertools.product(chars, repeat=size):
            print(cracked.join(i), hashlib.md5(cracked.join(i).encode('utf8')).hexdigest())

            if hashlib.md5(cracked.join(i).encode('utf8')).hexdigest() == data[j][1]:
                passwords.append(cracked.join(i))
                print("Password found >> " + '\'' + cracked.join(i) + '\'')
                break
    print(passwords)
    
crack(credentials, characters)
