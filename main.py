import hashlib
from data import *


def main():
    credential_file = 'credentials.txt'
    loop = True
    auth_loop = True

    while loop:
        m = hashlib.md5()
        credential_list = get_credentials(credential_file)
        existent_user = False
        username = str(input('Type a username: '))
        password = str(input('Type a password: '))

        assert len(username) <= 4, 'Max length of characters is 4'
        assert len(password) <= 4, 'Max length of characters is 4'

        m.update(password.encode('utf8'))
        md5_pw = m.hexdigest()

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
            loop = False

    while auth_loop:
        m = hashlib.md5()
        valid_credential = False
        credential_list = get_credentials(credential_file)
        username = str(input('Type your username: '))
        password = str(input('Type your password: '))

        m.update(password.encode('utf8'))
        md5_pw = m.hexdigest()

        for user in range(len(credential_list)):
            name = credential_list[user][0]
            pw = credential_list[user][1]
            if name.lower() == username.lower() and md5_pw == pw:
                valid_credential = True

        if valid_credential:
            print('Successfully authenticated!')
            auth_loop = False
        else:
            print('Invalid username or password')


if __name__ == '__main__':
    main()
