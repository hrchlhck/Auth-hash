import hashlib
import sys
import os
from data import *


def main():
    credential_file = 'credentials.txt'
    credential_list = get_credentials(credential_file)
    reg_loop = True
    auth_loop = True
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
                    md5_pw = hashlib.md5(password.encode('utf8')).hexdigest()

                    for user in range(len(credential_list)):
                        name = credential_list[user][0]
                        if name.lower() == username.lower():
                            existent_user = True

                    if existent_user:
                        print('This username already exists, please try again')
                    else:
                        with open(credential_file, 'a') as arq:
                            arq.write(username + ", " + md5_pw + '\n')
                            arq.close()
                            pass
                        print('Successfully registered!')
                        reg_loop = False
        elif option == 2:
            while auth_loop:
                valid_credential = False
                username = str(input('>> Type your username: '))
                password = str(input('>> Type your password: '))

                md5_pw = hashlib.md5(password.encode('utf8')).hexdigest()

                for user in range(len(credential_list)):
                    name = credential_list[user][0]
                    pw = credential_list[user][1]
                    if name.lower() == username.lower() and md5_pw == pw:
                        valid_credential = True

                if valid_credential:
                    print('Successfully authenticated!')
                    sys.exit()
                else:
                    print('Invalid username or password')
        elif option == 3:
            print('Good bye!')
            sys.exit()
        else:
            print('This option does not exist. Please, try again')


if __name__ == '__main__':
    main()
