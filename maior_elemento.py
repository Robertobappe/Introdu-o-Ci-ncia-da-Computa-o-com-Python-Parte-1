def maior_elemento(lista):
    a=len(lista)
    a=a-1
    i=0
    maior=-10000000000000000
    while i<=a:
        if lista[i]>=maior:
            maior=lista[i]
            i+=1
        else:
            i+=1
    return maior
