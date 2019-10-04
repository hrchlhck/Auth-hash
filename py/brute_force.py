from py.data import DataReader
import itertools
import hashlib
import time


def crack(target, chars, size=4):
    data = DataReader(target).get_data()
    cracked = ''
    passwords = []
    time_elapsed = []
    init_time = time.time()
    
    for j in range(len(size)):
        t0 = time.time()
        for i in itertools.product(chars, repeat=size):
            print(cracked.join(i), hashlib.md5(cracked.join(i).encode('utf8')).hexdigest())

            if hashlib.md5(cracked.join(i).encode('utf8')).hexdigest() == data[j][1]:
                passwords.append(cracked.join(i))
                print("Password found >> " + '\'' + cracked.join(i) + '\'')
                time_elapsed.append(time.time() - t0)
                break

    txt_format = 'Passwords found >> '
    for pw in passwords:
        txt_format += pw + ', '

    time_each_pw = ''
    for _time in time_elapsed:
        time_each_pw += str(_time) + ' seconds' + ', '

    print(txt_format)
    print(time_each_pw)
    print("Total time elapsed >> " + str(time.time() - init_time))
