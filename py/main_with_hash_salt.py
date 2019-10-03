from hashlib import md5
from sys import exit
from os import urandom
from data import DataReader
from base64 import b64encode

def main():
    data = DataReader('files/credentials.txt')
    credential_list = data.get_data()
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
                    salt = urandom(4)
                    salt_decoded = b64encode(salt).decode('utf8')
                    md5_pw = md5(password.encode('utf8') + salt).hexdigest()
        
                    for user in range(len(credential_list)):
                        name = credential_list[user][0]
                        if name.lower() == username.lower():
                            existent_user = True

                    if existent_user:
                        print('This username already exists, please try again')
                    else:
                        data.write_data(username, md5_pw, salt_decoded)
                        print('Successfully registered!')
                        reg_loop = False
        elif option == 2:
            while auth_loop:
                valid_credential = False
                username = str(input('>> Type your username: '))
                password = str(input('>> Type your password: '))

                md5_pw = md5(password.encode('utf8')).hexdigest()

                for user in range(len(credential_list)):
                    name = credential_list[user][0]
                    pw = credential_list[user][1]
                    salt = credential_list[user][2]
                    md5_pw_salt = md5(password.encode('utf8') + salt.encode('utf8')).hexdigest()
                    
                    if name.lower() == username.lower() and md5_pw_salt == pw:
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
