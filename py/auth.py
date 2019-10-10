from .data import DataReader
from hashlib import md5
import sys

data = DataReader('files/credentials.txt')

def sign_up(username, password, credential_list):
    reg_loop = True
    while reg_loop:
        existent_user = False

        if len(username) > 4 or len(password) > 4:
            raise ValueError('Username and password must be up to 4 characters only')
        else:
            md5_pw = md5(password.encode('utf8')).hexdigest()

            for user in range(len(credential_list)):
                name = credential_list[user][0]
                if name.lower() == username.lower():
                    existent_user = True

            if existent_user:
                print('This username already exists, please try again')
            else:
                data.write_data(username, md5_pw)
                print('Successfully registered!')
                reg_loop = False


def sign_in(username, password, credential_list):
    valid_credential = False
    md5_pw = md5(password.encode('utf8')).hexdigest()

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
