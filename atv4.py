verificar = input('digite seu quarto')

match verificar:
    case '':
        print('voce precisa colocar algo')
    case _:
        print('Ok, pode passar')

