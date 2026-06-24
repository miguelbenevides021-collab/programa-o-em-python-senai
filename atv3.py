num = int(input('Qual sua idade: '))

match num:
    case num if num <=12:
        print('é uma criança')
    case num if num >=13 and num <18:
        print('é adolecente')
    case num if num ==19 and num < 35:
        print('è jovem')
    case num if 35 < num <= 64:
        print('é adulto')
    case num if num >= 65:
        print('é idoso')

