import itertools
import string
import hashlib
import time
from data import *

letters = string.digits
credentials = 'credentials.txt'


def crack(target: str, size: int = 4) -> None:
    time_elapsed = 'Time elapsed: '
    pw = get_data(target, 1).splitlines()
    crack = ''
    while size > 0:
        time_init = time.time()
        for i in itertools.product(letters, repeat=size):
            crack = ''.join(i).encode('utf8')
            md5 = hashlib.md5(crack).hexdigest()
            if md5 == pw[size - 1]: # problem
                print(crack)
                time_elapsed += str(time.time() - time_init) + '\n'
                size -= 1
                break
            print(crack.decode('utf8'), md5)


crack('credentials.txt', 4)

