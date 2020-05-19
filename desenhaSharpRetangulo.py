largura = int(input("digite a largura:"))
altura = int(input("Digite a altura:"))
coluna = 1
linha = 1 

while linha <= altura:
    while coluna <= largura:
        print('#', end = "")
        coluna = coluna + 1
    print("")
    coluna = 1
    linha += 1 

