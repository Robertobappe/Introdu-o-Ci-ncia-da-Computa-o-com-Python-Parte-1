n=int(input("Digite um número inteiro: "))

i=1
a=False
b=False

while n!=1 and i<=n:
    i+=1
    if n!=i:
        if n%i!=0:
            a=True
        else:
            b=True
    else:
        a=True

if a==True and b==True:
    print("não primo")
    
else:
    print("primo")