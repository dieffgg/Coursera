import math

def delta(a, b, c):
    print ("Delta")
    return b ** 2 - 4 * a * c

def main():
    a = int(input("digite o valor de A:"))
    b = int(input("digite o valor de B:"))
    c = int(input("digite o valor de C:"))
    imprimir_raizes(a, b, c)

def imprimir_raizes(a, b, c):
    if delta(a, b, c) < 0:
        print("Não possui raizes reais")
    
    