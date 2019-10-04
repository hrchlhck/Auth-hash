import itertools
import string
import hashlib
import time
from data import DataReader

characters = string.digits + string.ascii_lowercase
credentials = 'files/credentials.txt'


def crack(target, chars, size=4):
    data = DataReader(target).get_data()
    cracked = ''
    passwords = []
    time_elapsed = []
    for j in range(1):
        t0 = time.time()
        for i in itertools.product(chars, repeat=size):
            md5_crack = hashlib.md5(cracked.join(i).encode('utf8')).hexdigest()
            print(cracked.join(i), md5_crack)
            if md5_crack == data[j][1]:
                passwords.append(cracked.join(i))
                print("Password found >> " + '\'' + cracked.join(i) + '\'')
                time_elapsed.append(time.time() - t0)
                break

    txt = 'Passwords found: '
    for _data in zip(time_elapsed, passwords):
        txt += str(_data) + ', '

        

def main():
    init_time = time.time()
    crack(credentials, characters)
    print("Total time elapsed >> " + str(time.time() - init_time))

if __name__ == '__main__':
    main()
