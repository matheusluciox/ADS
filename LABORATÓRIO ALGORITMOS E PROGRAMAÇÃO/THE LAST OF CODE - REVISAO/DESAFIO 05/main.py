'''
Crie um algoritmo que leia um arquivo e faça a soma apenas dos valores múltiplos de 3.

O código deverá ter tratamento de Exceção.
'''
with open('DESAFIO 05/valores.txt', 'r') as arquivo:
    multiplos_de_3 = []
    for linha in arquivo:
        try:
            numero = int(linha.strip())
            if numero % 3 == 0:
                multiplos_de_3.append(numero)
        except ValueError:
            print(f'Valor inválido: {linha.strip()}')
    
soma = sum(multiplos_de_3)

print(f'Os números multiplos de 3 são: {multiplos_de_3}')
print(f'A soma de todos eles é: {soma}')
