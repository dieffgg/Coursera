def fatorial(n):
    fatorial = 1 

    while n > 1: 
        fatorial = fatorial * n 
        n -= 1
    return fatorial

print (fatorial(5))