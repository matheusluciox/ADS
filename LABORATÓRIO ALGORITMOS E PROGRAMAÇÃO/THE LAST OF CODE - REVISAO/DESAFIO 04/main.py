'''
Crie um pacote que contenha 3 módulos:

verificar_par, multiplicar e subtrair.

Monte a estrutura das pastas, faça as funções, e teste em um arquivo main.
'''

from operacoes.multiplicar import *
from operacoes.subtrair import *
from operacoes.verificar_par import *

a = 5
b = 10
numero = 9

calculo_multiplicar = multiplicar(a, b)
calculo_subtrair = subtrair(a ,b)

print(f'A multiplicação do número é: {calculo_multiplicar}')
print(f'A subtração do número é: {calculo_subtrair}')
print(f'O número escolhido para ver se é par ou não foi {numero} e ele é {verificar_par(numero)}')