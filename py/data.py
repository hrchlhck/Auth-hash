import os

class DataReader:
    """
    Author: Pedro Horchulhack

    This class provides simple file writing and reading methods.
    
    Attributes:
        credential_file -- String containing the path plus filename which contains user + password data pattern
    
    Methods:
        get_data -> string
            Retrives all data in the file

        get_line_count -> integer
            Retrives the line count in the file

        write_data -> None
            Writes data into a text file separated by commas
    """

    def __init__(self, credential_file):
        self.credential_file = credential_file
        if not os.path.isfile(self.credential_file):
            open(self.credential_file, 'w+') 
        else:
            pass

    def get_data(self):
        try:
            with open(self.credential_file, 'r') as file:
                lines = ''
                line_lst = []

                # Adds data into a string
                for line in file.readlines():
                    lines += line

                str_lines = lines.splitlines()  # Responsible to separate the data into lines, resulting a list

                # Splits the list into smaller lists, where the data is username and password
                for i in str_lines:
                    line_lst.append(i.split(', '))
                file.close()
                return line_lst
        except FileNotFoundError:
            print('Unable to open file. It may not exist or it\'s corrupted.')

    def get_line_count(self):
        try:
            with open(self.credential_file, 'r') as file:            
                for index, line in enumerate(file):
                    pass
                file.close()
            return index + 1
        except FileNotFoundError:
            print('Unable to open file. It may not exist or it\'s corrupted.')

    def write_data(self, *args):
        try:
            with open(self.credential_file, 'a') as file:
                data = ''
                for _data in range(len(args)):
                    str_data = str(args[_data])
                    if _data < len(args) - 1:
                        data += str_data + ', '
                    elif _data == len(args) - 1:
                        data += str_data
                file.write(data + '\n')
                file.close()
        except FileNotFoundError:
            print('Unable to open file. It may not exist or it\'s corrupted.')
