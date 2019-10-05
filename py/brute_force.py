from py.data import DataReader
from itertools import product
from hashlib import md5
from time import time
import string
import os


class BruteForce:
    """
        Author: Pedro Horchulhack

        This class provide a simple way to crack md5 hashed passwords.

        Attributes:
            target -- string: File target containing hashed passwords;
            chars --  string: String containing all characters you may need to crack the passwords;
            size --     int:  Possible length of the unhashed password.

        Methods:
            crack -> String
                Retrives all the cracked passwords within the file you entered as input.

    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get the root folder of the project
    
    def __init__(self, target, chars, size):
        self.target = target
        self.chars = chars
        self.size = size

    def crack(self):
        data = DataReader(self.target).get_data()
        cracked = ''
        passwords = []
        time_elapsed = []
        for j in range(self.size):
            t0 = time()
            for i in product(self.chars, repeat=self.size):
                md5_attempt = md5(cracked.join(i).encode('utf8')).hexdigest()
                print(cracked.join(i), md5_attempt)

                if md5_attempt == data[j][1]:
                    passwords.append(cracked.join(i))
                    time_elapsed.append(time() - t0)
                    DataReader(self.path + '\\files\\cracked_passwords.txt').write_data(data[j][0], cracked.join(i))
                    break

        txt_format = 'Passwords found: '
        for y in zip(passwords, time_elapsed):
            txt_format += str('\n   ' + 'Password: ' + y[0] + ', time elapsed: ' + str(y[1]))
        return txt_format


def main():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    characters = string.digits + string.ascii_lowercase
    credentials = path + '\\files\\credentials.txt'

    init_time = time()
    print(BruteForce(credentials, characters, size=4).crack())
    print("Total time elapsed >> " + str(time() - init_time))


if __name__ == '__main__':
    main()
