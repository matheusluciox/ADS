'''
Função para Verificar Começo

- Escreva uma função verificar_inicio (texto) que recebe uma frase e verifica se ela começa com “Olá”.

- Deve mostrar pra o usuário se começa ou não com Olá
'''

def verificar_inicio():
    palavra = str(input('Digite a palavra: '))
    if palavra.startswith('Olá!'):
        print('Seu texto começa com Olá')
    else:
        print('Seu texto nao comeca com Olá')

verificar_inicio()