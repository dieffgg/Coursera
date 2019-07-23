# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não"

ndepois = n = int(input("Digite um número inteiro: "))
anterior = n % 10 
n = n // 10 
adj_iguais = False 

while n > 0 and not adj_iguais:
    proximo = n % 10 
    if anterior == proximo: 
        adj_iguais = True
    else: 
        anterior = proximo
        n = n // 10 

if adj_iguais:
    print("sim")
else: 
    print("não")

    