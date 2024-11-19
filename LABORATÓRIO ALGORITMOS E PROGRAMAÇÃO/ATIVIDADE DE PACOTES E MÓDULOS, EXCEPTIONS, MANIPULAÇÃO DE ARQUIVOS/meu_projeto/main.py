from aritmetica.operacoes import *
from geometria.formas import *

def salvar_resultado_linha(mensagem):
    with open("resultados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(mensagem + "\n")
    print(mensagem)

def ler_resultados():
    try:
        with open("resultados.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo 'resultados.txt':\n")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo 'resultados.txt' não encontrado. Por favor, execute as operações antes de tentar ler os resultados.")

def main():
    # RESETA OS TXT
    open("resultados.txt", "w", encoding="utf-8").close()
    
    ### SOMA ### // ### DIVISAO ###
    a = float(input("Digite o primeiro valor para somar e depois ser feito a divisão: "))
    b = float(input("Digite o segundo valor para somar e depois ser feito a divisão: "))
    salvar_resultado_linha(f"A soma de {a} e {b} é: {soma(a, b):.2f}")
    salvar_resultado_linha(f"A divisão de {a} e {b} é: {divisao(a, b):.2f}")
    
    ### AREA DO RETANGULO ###
    largura = float(input("Digite o valor da largura: "))
    altura = float(input("Digite o valor da altura: "))
    salvar_resultado_linha(f"A área do retângulo de largura {largura} e altura {altura} é: {area_retangulo(largura, altura):.2f}")
    
    ### CALCULAR RAIO ### // ### AREA DO CIRCULO ###
    raio = float(input("Digite o valor do raio do circulo: "))
    area = float(input("Digite o valor da área do circulo: "))
    salvar_resultado_linha(f"O calculo do raio do circulo é: {calcular_raio(raio):.2f}")
    salvar_resultado_linha(f"A area do circulo é: {area_circulo(area):.2f}")

    print("Resultados salvos em 'resultados.txt'.")

if __name__ == "__main__":
    main()
