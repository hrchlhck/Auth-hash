from py.data import DataReader
from py.auth import sign_in, sign_up
from py.brute_force import main as  bf_main

def main():
    data = DataReader('files/credentials.txt')
    print('Welcome! Choose an option: ')
    while True:
        print('(1) >> Sign up')
        print('(2) >> Log in')
        print('(3) >> Crack passwords')
        print('(4) >> Exit')
        option = int(input('>> '))
        
        credential_list = data.get_data()
        if option == 1:
            username = str(input('>> Type a username: '))
            password = str(input('>> Type a password: '))
            sign_up(username, password, credential_list)
        elif option == 2:
            username = str(input('>> Type your username: '))
            password = str(input('>> Type your password: '))
            sign_in(username, password, credential_list)
        elif option == 3:
            bf_main()
        elif option == 4:
            print('Good bye!')
            break
        else:
            print('This option does not exist. Please, try again')


if __name__ == '__main__':
    main()
