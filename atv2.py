n1 = (input('Digite seu numero>>>'))

try:
    if '.' in n1:
        print('erro')
    else:
        print('seu numero nao é um numero quebrado')
except ValueError:
    print('error seu numero é quebrado')
