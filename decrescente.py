def main():
    a = int(input("Digite o primeiro valor:"))
    b = int(input("Digite o segundo valor:"))
    c = int(input("Digite o terceiro valor:"))
    print (decrescente(a,b,c))


def decrescente(a,b,c):
    if a == b and b == c:
        print("numeros iguais")
        return "numeros iguais"
    elif a > b and a > c:
        if b > c:
            
            return a, b, c
        else:
            
            return a, c, b

    if b > a and b > c:
        if a > c:
            
            return b, a, c
        else:
            
            return b, c, a

    if c > a and c > b:
        if a > b:
            
            return c, a, b
        else:
            
            return c, b, a

main()
