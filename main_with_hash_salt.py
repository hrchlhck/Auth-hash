from py.data import DataReader
from base64 import b64encode
from time import sleep
import hashlib
import sys
import os


def main():
    data = DataReader('files/credentials_salt.txt')
    credential_list = data.get_data()
    reg_loop = True
    auth_loop = True
    encode_type = 'utf8'
    print('Welcome! Choose an option: ')
    while True:
        print('(1) >> Sign up')
        print('(2) >> Log in')
        print('(3) >> Exit')
        option = int(input('>> '))

        if option == 1:
            while reg_loop:
                existent_user = False
                username = str(input('>> Type a username: '))
                password = str(input('>> Type a password: '))

                if len(username) > 4 or len(password) > 4:
                    raise ValueError('Username and password must be up to 4 characters only')
                else:
                    salt = b64encode(os.urandom(4)) # Generates random bytes and decode them to printable characters
                    salt = salt.decode(encode_type)
                    MD5 = hashlib.md5(salt.encode(encode_type) + password.encode(encode_type)).hexdigest()
        
                    for user in range(len(credential_list)):
                        name = credential_list[user][0]
                        if name.lower() == username.lower():
                            existent_user = True

                    if existent_user:
                        print('This username already exists, please try again')
                    else:
                        data.write_data(username, MD5, salt)
                        print('Successfully registered!')
                        break
        elif option == 2:
            while auth_loop:
                valid_credential = False
                username = str(input('>> Type your username: '))
                password = str(input('>> Type your password: '))

                for user in range(len(credential_list)):
                    name = credential_list[user][0]
                    pw = credential_list[user][1]
                    salt = credential_list[user][2]
                    MD5 = hashlib.md5(salt.encode(encode_type) + password.encode(encode_type)).hexdigest()
                    
                    if name.lower() == username.lower() and MD5 == pw:
                        valid_credential = True

                if valid_credential:
                    print('Successfully authenticated!')
                    sys.exit()
                else:
                    print('Invalid username or password')
        elif option == 3:
            print('Good bye!')
            break
        else:
            print('This option does not exist. Please, try again')


if __name__ == '__main__':
    main()
