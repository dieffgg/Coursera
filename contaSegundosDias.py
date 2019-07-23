seg = int(input("Digite os segundos: "))

a = seg // 86400
b = (seg // 3600) % 24
c = (seg // 60) % 60
d = seg % 60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")