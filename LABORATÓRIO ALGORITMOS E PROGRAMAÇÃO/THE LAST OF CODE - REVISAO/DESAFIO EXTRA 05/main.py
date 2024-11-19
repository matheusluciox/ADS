'''
Solicite ao usuário 10 vezes, os seguinte inputs:
Usuário digita um número (N1);
Usuário digita outro número (N2);

O algoritmo deve fazer a multiplicação do N1 por N2 e salvar em um arquivo multiplicados.txt

O algoritmo deve prever e tratar exceções
'''

def salvar_multiplicacoes():
    with open('DESAFIO EXTRA 05/multiplicados.txt', 'w') as arquivo:
        for i in range(10):
            try:
                n1 = float(input(f'Digite o número {i + 1} (N1): '))
                n2 = float(input(f'Digite o número {i + 1} (N2): '))
                resultado = n1 * n2
                arquivo.write(f'{n1} x {n2} = {resultado}\n')
            except ValueError:
                print('Erro: Você deve digitar números válidos. Tente novamente.')

salvar_multiplicacoes()
