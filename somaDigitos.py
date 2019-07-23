# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

n = int(input("Digite o valor de n: "))
soma = 0 

while n > 0: 
    soma = soma + (n % 10)
    n = n // 10 

print(soma)

# Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.
    