listaDeccompras = ['','hamburguer', 'sorvete', 'fornalha']

print('hamburguer')
print('sorvete')
print('fornalha')



try:
    
    esolha = int(input('escolha suas compras: '))
    if esolha <= 3 and esolha >0:
        res = listaDeccompras[esolha]
        print(f'voce escolheu {res}')
    else:
        print('Erro: Esse número de produto não existe na lista!')
except:
        print('Erro: Você não digitou um número válido!')

