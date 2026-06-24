escolha = ['','miguel', 'matheus', 'idiota']

print('miguel')
print('matheus')
print('idiota')
opusuario = int(input('escolha um da lista '))

res = escolha[opusuario]

if res == 'miguel' :
    print('otima escolha')
elif res == 'matheus':
    print('escolha ok')
else:
    print('da para passar!')