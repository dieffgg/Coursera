peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso / (altura ** 2)

if imc > 17 and imc < 18.49:
    print("Abaixo do peso",imc)
elif imc > 18.5 and imc < 24.99:
    print("Peso normal", imc)
elif imc > 25 and imc < 29.99: 
    print("Acima do peso",imc)
elif imc > 30 and imc < 34.99:
    print("Obesidade I",imc)
elif imc > 35 and imc < 39.99:
    print("Obesidade severa",imc)
else:
    print("Obesidade Mórbida, vá se cuidar",imc)
