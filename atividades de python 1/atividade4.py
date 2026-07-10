n1 = int(input('1 - digite seu numero'))
n2 = int(input('2 - digite seu numero'))
n3 = int(input('3 - digite seu numero'))

if n1 == n2 == n3 == n1:
    print('é um equilatero')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('Isósceles')
else:
    print('Escaleno')