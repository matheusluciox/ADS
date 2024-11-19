def divisao(valor, divisor=2):
    try:
        resultado = valor / divisor
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
