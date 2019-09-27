import itertools
import string
import hashlib
import time
from data import *

letters = string.printable
credentials = 'credentials.txt'


def crack_hash(target, size=4):
    """
    :param target: Path to data file
    :param size: size of the password
    :return: itself
    """
    passwords = get_data(target, 1).splitlines()
    cracked = ''
    if size <= 0:
        return cracked
    else:
        for i in itertools.product(letters, repeat=size):
            cracked = ''.join(i).encode('utf8')
            if hashlib.md5(cracked).hexdigest() == passwords:
                print(cracked)
                return cracked
        return crack_hash(target, size - 1)
    pass




def test():
    pw = get_data(credentials, 1).splitlines()
    crack = ''
    pw_size = 4
    while pw_size > 0:
        for i in itertools.product(letters, repeat=4):
            crack = ''.join(i).encode('utf8')
            md5 = hashlib.md5(crack).hexdigest()
            if md5 == pw[pw_size - 1]:
                print(crack)
                pw_size -= 1
            print(crack.decode('utf8'), md5)

test()

