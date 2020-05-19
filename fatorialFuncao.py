def fatorial(n):
    fatorial = 1 

    while n > 1: 
        fatorial = fatorial * n 
        n -= 1
    return fatorial

def main():
    n = int(input("Digite um numero inteiro:"))

    while n >= 0:
        print (fatorial(n))
        n = int(input("Digite um numero inteiro:"))

main()
fatorial(5)