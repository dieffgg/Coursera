largura = int(input("digite a largura:"))
altura = int(input("Digite a altura:"))
coluna = 1
linha = 1 

while linha <= altura:
    while coluna <= largura:
        if linha == 2:
            if coluna >= 2 and coluna < largura:
                print(' ', end = "")
            else: 
                print('#',end = "")
        else:    
            print('#', end = "")
        coluna = coluna + 1
    print("")
    coluna = 1
    linha += 1 

