'''
Para instalar, seguir instrucoes do site:
https://docs.pytest.org/en/latest/getting-started.html

documentacao:
https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf

Ferramenta que ajuda a escrever testes para python. Ajuda a escrever programas melhores
    - Existe uma convencao do nome do arquivo. Ex.: *_test ou test_* 


Para testar, vai na pasta atraves do comand do windows e escreva
pytest test_fatoria.py
pytest -q test_fatoria.py (modo quiet)
'''
import pytest

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


def eh_par(num):
    if num % 2 == 0:
        return True
    return False

def test_fatorial():
    assert fatorial(0) ==1

def test_eh_par():
    assert eh_par(10) == True