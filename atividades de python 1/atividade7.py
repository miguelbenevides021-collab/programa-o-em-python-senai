n1 = int(input('Digite seu numero'))

if n1 > 0 and (n1 % 5 == 0 or n1 % 3 == 0):
    print('este numero é divisivel por 5 ou 7')
else:
    print('não é divido nem por 7 e nem por 5')
