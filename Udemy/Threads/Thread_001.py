'''
Thread:
    - uma forma de um processo dividir a si proprio em duas ou mais tarefas simultaneas

'''

from threading import Thread    #biblioteca de Thread
import time                     #para colocar sleep em alguns momentos


def func(i):
    print('Iniciando a thread %d' % i)
    time.sleep(2)
    print('Thread %d finalizada' % i)


#criando 10 Threads
for i in range(10):
    #primeiro argumento aponta a funcao que executara em Thread, e argumento args=(i,)
    t = Thread(target=func, args=(i,))  #para funcionar tem que ter a virgula depois de i?
    t.start()