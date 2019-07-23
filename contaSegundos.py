segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400 
segRestantes = segundos % 86400 
horas = segRestantes // 3600 
segRestantes2 = segRestantes % 3600 
minutos = segRestantes2 // 60 
segRestantes3 = segRestantes2 % 60 

print(dias, horas, minutos)