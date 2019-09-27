def get_credentials(credential_file):
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


def get_data(credential_file, type=0):
    """
    :param credential_file: String that indicates the path of the file containing data
    :param type: 0 for username, 1 for password
    :return: string
    """
    pw = get_credentials(credential_file)
    passwords = ''
    if type == 0:
        for i in range(len(pw)):
            passwords += pw[i][type] + '\n'
    elif type == 1:
        for i in range(len(pw)):
            passwords += pw[i][type] + '\n'
    else:
        raise IndexError('Max length is 2')
    return passwords


# print(retornar_dados('credentials.txt', 2))
