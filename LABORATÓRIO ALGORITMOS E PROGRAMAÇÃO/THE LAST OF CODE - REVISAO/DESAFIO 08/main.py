'''
Crie um algoritmo que leia as palavras de um arquivo e salve em outro arquivo as palavras que começam com B e terminam com O
'''
palavras_validas = []

with open('DESAFIO 08/arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.startswith(('B', 'o')):
            palavra = str(linha.strip())
            palavras_validas.append(palavra)

with open('DESAFIO 08/palavras_validas.txt', 'w') as arquivo:
    for palavra in palavras_validas:
        arquivo.writelines(palavra)
print("As palavras válidas foram salvas em 'palavras_validas.txt'.")