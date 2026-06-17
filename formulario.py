concordar = "sim"

print('Faça seu cadastro!')


def cadastro():
    nome = input('Qual seu Nome?')
    print('Dados salvo')
    email = input('Qual seu Nome?')
    print('Dados salvo')
    idade = int(input('qual a sua idade?'))
    print('Dados salvo')
    cidade = input('sua cidade?')
    print('Dados salvo')
    graduação = input('qual a sua graduação?')
    print('Dados salvo')
    estado = input('qual a seu estado civil?')

    verdados = input('Gostaria de ver seus dados?').lower()


    if concordar:
        print(nome)
        print(email)
        print(idade)
        print(cidade)
        print(graduação)
        print(estado)
    else:
        print('Thau!')
cadastro()








