'''
Solicite ao usuário 10 vezes, os seguinte inputs:
Usuário digita um número (N1);
Usuário digita outro número (N2);

O algoritmo deve fazer a divisão do N1 por N2 e salvar em um arquivo divisão.txt

O algoritmo deve prever e tratar exceções
'''

def main():
    with open('DESAFIO EXTRA 04/divisao.txt', 'w', encoding='utf-8') as arquivo:
        for x in range(10):
            try:
                n1 = float(input(f'Digite o {x + 1}º número (N1): '))
                n2 = float(input(f'Digite o {x + 1}º número (N2): '))
                
                resultado = n1 / n2
                arquivo.write(f'Divisão {x + 1}: {n1} / {n2} = {resultado:.2f}\n')
                print(f'Resultado: {resultado:.2f}')
            
            except ZeroDivisionError:
                print('Erro: Divisão por zero não é permitida.')
                arquivo.write(f'Divisão {x + 1}: Erro - Divisão por zero\n')

main()
