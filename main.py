# dicionarios

estoque = {

        'livros': {
                        'livro 1':10.0,
                        'livro 2': 20.55,
                        'livro 3':50.60
                    },

        'tablest':{
                    't1':500.50,
                    't2':250.90,
                    't3':470.30
                    },

        'fones':  {
                    'fone 1':126.50,
                    'fone 2':450.0,
                    'fone 3':155.60
                    }
}


# senha = input()


carrinho = []
total = []

sec = input(f'seção 🗽:{str(estoque.keys())}: ')
print('Você acessou a seção: ', estoque[sec])
prod = input(f'escolha produto:')
print('Adicionar ao carrinho: 🛒🛒',prod)
carrinho.append(prod)
total.append(estoque[sec][prod])

sec = input(f'seção:{estoque.keys()}: ')
print('Você acessou a seção: ', estoque[sec])
prod = input(f'escolha produto:')
print('Adicionar ao carrinho: 🛒🛒',prod)
carrinho.append(prod)
total.append(estoque[sec][prod])

soma  = sum(total)
print('R$', soma)
print(carrinho)
lista = ['', '1 - PIX', '2 - CC', '3 - CD']
pag =  int(input(f'Escolha a forma de pagamento: {lista}'))
print('Sua forma de pagamento é ', pag)
print('Obrigada Volte Sempre!')

input('Digite enter sair ⌨️... ')