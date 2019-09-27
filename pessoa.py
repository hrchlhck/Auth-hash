import hashlib
from arquivo import listar_credenciais


def main():
    arq_credenciais = 'credenciais.txt'
    loop = True
    loop_autenticacao = True

    while loop:
        m = hashlib.md5()
        lista_credenciais = listar_credenciais(arq_credenciais)
        usuario_existente = False
        username = str(input('Insira um nome de usuário: '))
        password = str(input('Insira uma senha: '))

        assert len(username) <= 4, 'O máximo de caracteres permitido é 4'
        assert len(password) <= 4, 'O máximo de caracteres permitido é 4'

        m.update(password.encode('utf8'))
        senha_md5 = m.hexdigest()

        for usuario in range(len(lista_credenciais)):
            nome = lista_credenciais[usuario][0]
            if nome.lower() == username.lower():
                usuario_existente = True

        if usuario_existente:
            print('Nome de usuário já existente, tente novamente')
        else:
            with open(arq_credenciais, 'a') as arq:
                arq.write(username + ", " + senha_md5 + '\n')
                arq.close()
                pass
            print('Usuário cadastrado com sucesso!')
            loop = False

    while loop_autenticacao:
        m = hashlib.md5()
        credencial_valida = False
        lista_credenciais = listar_credenciais(arq_credenciais)
        username = str(input('Digite seu nome de usuário: '))
        password = str(input('Digite sua senha: '))

        m.update(password.encode('utf8'))
        senha_md5 = m.hexdigest()

        for usuario in range(len(lista_credenciais)):
            nome = lista_credenciais[usuario][0]
            senha = lista_credenciais[usuario][1]
            if nome.lower() == username.lower() and senha_md5 == senha:
                credencial_valida = True

        if credencial_valida:
            print('Login realizado com sucesso!')
            loop_autenticacao = False
        else:
            print('Login ou senha inválido. Tente novamente.')


if __name__ == '__main__':
    main()
