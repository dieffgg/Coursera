def fatoresPrimos(n):
    n = int(input("Digite um numero inteiro:"))
    fator = 2
    multip = 0 

    while n > 1:
        while n % fator == 0:
            multip += 1
            n = n / fator
        if multip > 0:
            print("Fator ", fator,"Multiplicidade:",multip)
        fator += 1 
        multip = 0 

fatoresPrimos(100)