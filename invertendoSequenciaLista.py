lista = []
n = 1

while n > 0:
    n = int(input("Digite os valores:"))
    lista.append(n)
lista = [i for i in lista[::-1]]
lista.remove(0)

for i in lista:
    print(i)
    