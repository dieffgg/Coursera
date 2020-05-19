# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

num = n = int(input("Digite um número inteiro: "))
num -= 1 
cont = 2 
numeroPrimo = True 

while num < n and numeroPrimo:
    numeroPrimo = not ((num % cont)== 0)
    cont = cont + 1 
    if numeroPrimo:
        print(num)
    else: 
        print("não primo")    

    