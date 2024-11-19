# Crie um algoritmo que leia um arquivo e exiba as palavras terminadas em a.

palavras_terminadas = []
with open('DESAFIO EXTRA 02/arquivo.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.endswith(('a')):
            palavra = str(linha.strip())
            palavras_terminadas.append(palavra)

print(f"As palavras terminadas em 'a' foram: {palavras_terminadas}")