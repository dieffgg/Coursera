def tabuada():
    linha = 0 
    coluna = 0
    
    while linha < 10:
        linha = linha + 1
        while coluna < 10:
            coluna = coluna + 1
            print (coluna * linha, end="\t")
        print()   
        coluna = 0
        

tabuada()
