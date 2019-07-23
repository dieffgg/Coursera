num = n = int(input("Digite um número inteiro: "))
cont = 2
num = num - 1
numeroPrimo = True 

while num < n and numeroPrimo:
    numeroPrimo = not ((num % cont)== 0)
    num = num - 1 

if numeroPrimo:
    print(num)
else: 
    print(num)

    