s=int(input("Por favor, entre com o número de segundos que deseja converter:"))

d=s//(24*3600)
x=s%(24*3600)
h=x//3600
y=x%3600
m=y//60
s=y%60

print(d,"dias,",h,"horas,",m,"minutos e",s,"segundos.")