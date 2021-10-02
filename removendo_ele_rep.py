def remove_repetidos(lista):
    a=len(lista)
    a=a-1
    i=0
    j=1
    while i<=a:
        while j<=a:
            if lista[i]==lista[j]:
                del(lista[j])
                a=len(lista)
                a=a-1
                i=0
                j=1
            else:
                j+=1
        i+=1
        j=i+1
    lista.sort()
    return lista
    
