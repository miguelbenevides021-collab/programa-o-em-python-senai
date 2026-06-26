print('Sistema de compras!')

compras = ['','coca-cola','shanduiche', 'bacon', 'marmita']

print('coca-cola')
print('shanduiche')
print('bacon')
print('marmita')

def opcompras():
    for i in range(3):
        try:
            escolha = int(input('qual voce escolhe?: '))

            escolhausuario = compras[escolha]

            print(f'sua escolha foi: {escolhausuario}')
        except ValueError:
            con = input('error 400: Aconteceu um erro, deseja continuar?').lower()
            if con == 'sim':
                opcompras()
            else:
                input('enter para sair')
                break
opcompras()
          
