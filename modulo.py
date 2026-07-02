import random
import time

def numeros2():
    x = random.randint(5,10)
    return x

def numeros3():
    x = random.randint(0,10)
    y = random.randint(0,10)
    z = random.randint(0,10)

    return x, y, z


def numero4():
    x = random.choice(range(10,30))
    return x

def contagem():
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)
    print('fogo')


def pares():
    limite = int(input('Digite seu numero>>'))
    soma = 0
    
    for i in range(2, limite + 1, 2):
        soma = soma + i
    return soma


def multi():
    n1 = int(input('digite seu numero inteiro: '))
    for i in range(10,0, -1):
        soma = n1 * i
        print(f'{n1} x {i} ={soma}')

   

def contagem99():
    for i in range(99, 0 , -2):
        time.sleep(1)
        print(i)
pares()