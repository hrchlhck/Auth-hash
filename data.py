def get_credentials(credential_file):
    try:
        with open(credential_file, 'r') as file:
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


def get_data(credential_file, _type=0):
    """
    :param credential_file: String that indicates the path of the file containing data
    :param _type: 0 for username, 1 for password
    :return: string
    """
    pw = get_credentials(credential_file)
    passwords = ''
    if _type == 0:
        for i in range(len(pw)):
            passwords += pw[i][_type] + '\n'
    elif _type == 1:
        for i in range(len(pw)):
            passwords += pw[i][_type] + '\n'
    else:
        raise IndexError('Max length is 2')
    return passwords


def get_line_count(credential_file):
    """
        :param credential_file: String containing the path plus filename which contains user + password data pattern
        :return: Integer that represent the line count in the file
    """
    try:
        with open(credential_file, 'r') as file:            
            for index, line in enumerate(file):
                pass
        return index + 1
    except FileNotFoundError:
        print('Unable to open file. It may not exist or it\'s corrupted.')

