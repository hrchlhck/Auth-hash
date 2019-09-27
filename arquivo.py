def listar_credenciais(arq_credenciais):
    with open(arq_credenciais, 'r') as arq:
        linhas = ''
        _linhas_lst = []

        # Adiciona os dados de um txt dentro de uma string
        for linha in arq.readlines():
            linhas += linha

        linhas_str = linhas.splitlines()  # Responsável por separar a string em linhas, resultando numa lista

        # Separa a lista em pares de string, que corresponde ao login e senha respectivamente
        for i in linhas_str:
            _linhas_lst.append(i.split(', '))
        arq.close()
        return _linhas_lst


def retornar_dados(arq_credenciais, tipo=0):
    """
    :param arq_credenciais: String that indicates the path of the file containing data
    :param tipo: 0 for username, 1 for password
    :return: string
    """
    pw = listar_credenciais(arq_credenciais)
    senhas = ''
    if tipo == 0:
        for i in range(len(pw)):
            senhas += pw[i][tipo]
    elif tipo == 1:
        for i in range(len(pw)):
            senhas += pw[i][tipo]
    else:
        raise IndexError('O tamanho máximo é 2')
    return senhas
