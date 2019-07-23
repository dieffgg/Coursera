def triangulo(a,b,c):
    if a > b + c and b > a + c and c > a + b:
        return False
    elif a == b and b == c: 
        return "equilatero"
    elif a == b or a == c or b == c:
        return "Isóceles"
    else:
        return "Escaleno"


print(triangulo(5,3,1))
    

        