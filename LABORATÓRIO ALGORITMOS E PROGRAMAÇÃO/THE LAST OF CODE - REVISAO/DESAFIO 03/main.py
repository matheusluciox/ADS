'''
Função para Criar e Escrever em um Arquivo

- Escreva uma função criar_arquivo(nome_arquivo, conteudo) que cria um arquivo .txt e escreve o conteúdo dentro dele. O conteúdo deverá ser digitado pelo usuário.
'''

# 'r': leitura (o arquivo deve existir).
# 'w': escrita (cria um novo arquivo ou sobrescreve um existente).
# 'a': anexar (adiciona conteúdo ao final do arquivo).
# 'rb'/'wb': leitura/escrita em modo binário.

def criar_arquivo():
    with open('DESAFIO 03/arquivo.txt', 'w', encoding='utf-8') as arquivo:
        texto = input('Digite o texto: ')
        arquivo.writelines(texto)
        print('Finalizado com sucesso!')

criar_arquivo()