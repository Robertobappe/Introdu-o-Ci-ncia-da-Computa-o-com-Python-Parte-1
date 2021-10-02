def soma_elementos(lista):
    a=len(lista)
    a=a-1
    i=0
    j=1
    b=lista[0]
    while j<=a:
        b+=lista[j]
        j+=1
    return b
