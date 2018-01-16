'''
Criando um teste unitario
'''
import unittest

def fat(n):
    if n == 0:
        return 1
    return n * fat(n-1)


def pot(base, exp):
    if exp==0:
        return 1
    #decrementando o expoente ate que chegue a zero
    return base * pot(base, exp -1) 

#criando uma classe de teste, herdando o testCase, para utilizar os metodos de testCase (assertEqual, assertTrue, etc)
class TestMathMethods(unittest.TestCase):
    def test_pot(self):
        self.assertEqual(1024, pot(2,10))

    def test_fat(self):
        self.assertEqual(24, fat(4))


#para executar os testes
unittest.main()