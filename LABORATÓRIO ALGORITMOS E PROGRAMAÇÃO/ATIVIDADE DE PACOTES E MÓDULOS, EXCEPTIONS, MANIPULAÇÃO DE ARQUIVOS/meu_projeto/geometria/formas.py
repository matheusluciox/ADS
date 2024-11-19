pi = 3.14

def area_retangulo(largura, altura):
    return largura * altura

def calcular_raio(area):
    raio = (area / pi) ** 0.5
    return raio

def area_circulo(raio):
    area = pi * raio ** 2
    return area