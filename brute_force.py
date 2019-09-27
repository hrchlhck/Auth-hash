import itertools
import string
import hashlib
import time
from arquivo import *

letras = string.printable


def ataque(alvo, tamanho=4):
    senhas = retornar_dados(alvo, 1)
    for i in itertools.product(letras, repeat=tamanho):
        senha = ''.join(i).encode('utf8')
        if hashlib.md5(senha).hexdigest() == senhas:
            return senha
    return ataque(alvo, tamanho + 1)



