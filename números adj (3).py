n=int(input("Digite um número inteiro: "))

ultimo=-5
penultimo=-7
y=False
x=False

while n>=10:
    ultimo=n%10
    n=n//10
    penultimo=n%10
    if ultimo==penultimo:
        y=True
    else:
        x=False
if y==True:
    print("sim")
else:
    print("não")
    

