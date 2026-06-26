n1 = int(input('Digite numero 1>>>>'))
n2 = int(input('Digite numero 2>>>'))
try:
    print(n1/n2)
except ZeroDivisionError:
    print('error ao fazer a divisão')