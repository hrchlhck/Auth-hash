import itertools
import string
import hashlib
import time
from data import *

letters = string.printable


def crack_hash(target, size=4):
    passwords = get_data(target, 1).splitlines()
    for i in itertools.product(letters, repeat=size):
        pw = ''.join(i).encode('utf8')
        if hashlib.md5(pw).hexdigest() == passwords:
            return pw
    return crack_hash(target, size + 1)



