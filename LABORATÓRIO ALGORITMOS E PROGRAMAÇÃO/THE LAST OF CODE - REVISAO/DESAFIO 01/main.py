'''' 
Criar um Módulo Básico

Crie um módulo chamado operacoes.py com uma função somar(a, b) que retorna a soma de a e b.

Teste dentro de um arquivo main.py
'''

from operacoes.soma import *

a = 5
b = 10

calculo_soma = soma(a, b)

print(f'A soma do número {a} + {b} é igual a: {calculo_soma}')

