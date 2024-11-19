'''
Agora crie um algoritmo que leia um arquivo e mostre na tela as palavras dentro dele que começam com a letra M e terminam com A.
'''

def palavras_com_m_e_a():
    with open('DESAFIO EXTRA 06/arquivo.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        palavras_filtradas = []
        for palavra in palavras:
            if palavra.lower().startswith('m') and palavra.lower().endswith('a'):
                palavras_filtradas.append(palavra)
        print('Palavras que começam com "M" e terminam com "A":')
        for palavra in palavras_filtradas:
            print(palavra)

palavras_com_m_e_a()