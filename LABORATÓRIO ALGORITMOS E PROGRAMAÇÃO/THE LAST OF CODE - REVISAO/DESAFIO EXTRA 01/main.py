'''
Crie um pacote que contenha o módulo de divisão. 
Crie a função para tal módulo e faça tratamento de exceção para divisões por zero.
Depois no arquivo main.py, faça a leitura de um arquivo chamado valores.txt e use a função criada anteriormente para dividir o valor de cada linha por 2. Faça tratamento das exceções no main.py também. 
'''
from operacoes.divisao import *

def ler_e_dividir_arquivo():
    with open('DESAFIO EXTRA 01/valores.txt', 'r') as arquivo:
        for linha in arquivo:
            valor = float(linha.strip())
            resultado = divisao(valor)
            print(f"{valor} dividido por 2 é igual a: {resultado}")

ler_e_dividir_arquivo()

